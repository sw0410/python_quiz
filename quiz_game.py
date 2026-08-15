import json
import os
import sys
import random


# 분리된 quiz.py 모듈에서 Quiz 클래스와 DEFAULT_QUIZZES 가져오기
from quiz import DEFAULT_QUIZZES, Quiz

STATE_FILE = "state.json"

# ==========================================
# QuizGame 클래스 (전체 게임 제어 및 관리)
# ==========================================
class QuizGame:
    """게임 전체 흐름, 상태 관리 및 영속성을 총괄하는 클래스"""

    def __init__(self):
        self.quizzes: list[Quiz] = []
        self.best_score: int = 0
        self.load_state()  # 저장된 상태 불러오기

    def load_state(self):
        """state.json 파일에서 퀴즈 데이터와 최고 점수를 불러옴 (예외 처리 포함)"""
        if not os.path.exists(STATE_FILE):
            # 파일이 없으면 기본 데이터 사용 및 생성
            self.quizzes = list(DEFAULT_QUIZZES)
            self.best_score = 0
            self.save_state()
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                self.best_score = data.get("best_score", 0)

                # 파일은 존재하지만 퀴즈 데이터가 비어있는 경우 기본값 복구
                if not self.quizzes:
                    self.quizzes = list(DEFAULT_QUIZZES)

        except (json.JSONDecodeError, KeyError, Exception):
            # 파일이 손상되었거나 형식이 올바르지 않은 경우
            print("\n⚠️ state.json 파일이 손상되었습니다. 기본 데이터로 복구합니다.")
            self.quizzes = list(DEFAULT_QUIZZES)
            self.best_score = 0
            self.save_state()

    def save_state(self):
        """state.json 파일에 현재 상태(퀴즈 목록, 최고 점수)를 저장"""
        try:
            data = {
                "quizzes": [q.to_dict() for q in self.quizzes],
                "best_score": self.best_score
            }
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"\n⚠️ 데이터 저장 중 오류가 발생했습니다: {e}")

    def display_menu(self):
        """메인 메뉴 출력"""
        print("\n" + "=" * 30)
        print("       PYTHON QUIZ GAME")
        print("=" * 30)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 퀴즈 삭제")
        print("5. 최고 점수 확인")
        print("6. 종료")
        print("=" * 30)

    def get_valid_input(self, prompt: str, min_val: int, max_val: int) -> int:
        """공통 입력 검증 메서드"""
        while True:
            try:
                user_input = input(prompt).strip()

                if not user_input:
                    print("⚠️ 입력이 비어 있습니다. 다시 입력해 주세요.")
                    continue

                choice = int(user_input)

                if min_val <= choice <= max_val:
                    return choice
                else:
                    print(f"⚠️ {min_val}~{max_val} 사이의 숫자를 입력해 주세요.")

            except ValueError:
                print("⚠️ 숫자로만 입력해 주세요. (예: 1)")

    def run(self):
        """메인 게임 루프 실행"""
        try:
            while True:
                self.display_menu()
                choice = self.get_valid_input("메뉴를 선택하세요: ", 1, 5)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:    
                    self.delete_quiz()
                elif choice == 5:
                    self.show_best_score()
                elif choice == 6:
                    self.save_state()
                    print("\n게임을 종료합니다. 이용해 주셔서 감사합니다!")
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 프로그램이 강제 종료 요청을 받았습니다.")
            self.save_state()
            print("안전하게 데이터를 저장 후 종료합니다.")
            sys.exit(0)

    def play_quiz(self):
        """1. 퀴즈 풀기 기능 구현"""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        print("\n" + "=" * 30)
        print("         퀴즈 풀기 시작")
        print("=" * 30)
        
        # 문제 순서 랜덤 셔플
        shuffled_quizzes = list(self.quizzes)
        random.shuffle(shuffled_quizzes)        

        current_score = 0
        total_quizzes = len(shuffled_quizzes)

        for idx, quiz in enumerate(shuffled_quizzes, 1):
            print(f"\n[문제 {idx}/{total_quizzes}] {quiz.question}")
            for i, choice in enumerate(quiz.choices, 1):
                print(f"  {i}. {choice}")

            user_choice = self.get_valid_input("정답 번호를 입력하세요 (1~4): ", 1, 4)

            if quiz.is_correct(user_choice):
                print("⭕ 정답입니다!")
                current_score += 1
            else:
                print(f"❌ 오답입니다. (정답: {quiz.answer}번)")

        print("\n" + "=" * 30)
        print(f"🎉 모든 문제를 풀었습니다!")
        print(f"최종 점수: {current_score} / {total_quizzes}")

        if current_score > self.best_score:
            print(f"🎊 축하합니다! 새로운 최고 점수 달성! ({self.best_score}점 ➡️ {current_score}점)")
            self.best_score = current_score
            self.save_state()  # 최고 점수 갱신 시 자동 저장
        else:
            print(f"현재 최고 점수: {self.best_score}점")
        print("=" * 30)

    def add_quiz(self):
        """2. 퀴즈 추가 기능 구현"""
        print("\n" + "=" * 30)
        print("          새 퀴즈 등록")
        print("=" * 30)

        # 문제 입력 검증
        while True:
            question = input("문제 내용을 입력하세요: ").strip()
            if question:
                break
            print("⚠️ 문제 내용은 비어 둘 수 없습니다.")

        # 선택지 4개 입력받기
        choices = []
        for i in range(1, 5):
            while True:
                choice_text = input(f"선택지 {i}번: ").strip()
                if choice_text:
                    choices.append(choice_text)
                    break
                print("⚠️ 선택지 내용은 비어 둘 수 없습니다.")

        # 정답 번호 입력받기
        answer = self.get_valid_input("정답 번호를 입력하세요 (1~4): ", 1, 4)

        # 퀴즈 객체 생성 및 목록 추가
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()  # 즉시 파일 저장

        print("\n✅ 새로운 퀴즈가 성공적으로 등록되었습니다!")

    def show_quiz_list(self):
        """3. 퀴즈 목록 조회 기능 구현"""
        if not self.quizzes:
            print("\n⚠️ 저장된 퀴즈가 없습니다.")
            return

        print("\n" + "=" * 30)
        print(f"      등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("=" * 30)

        for idx, quiz in enumerate(self.quizzes, 1):
            print(f"\n[{idx}] {quiz.question}")
            for i, choice in enumerate(quiz.choices, 1):
                print(f"   {i}) {choice}")
            print(f"   👉 정답: {quiz.answer}번")

    def show_best_score(self):
        """4. 최고 점수 확인 기능 구현"""
        print("\n" + "=" * 30)
        print("           최고 점수")
        print("=" * 30)
        if self.best_score == 0:
            print("아직 기록된 최고 점수가 없습니다. 퀴즈를 풀어보세요!")
        else:
            print(f"🏆 현재 최고 점수: {self.best_score}점")
        print("=" * 30)

    def delete_quiz(self):
        """등록된 퀴즈를 선택하여 삭제하고 state.json에 반영"""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        print("\n" + "=" * 30)
        print("          퀴즈 삭제")
        print("=" * 30)

        # 현재 등록된 퀴즈 목록 번호와 함께 출력
        for idx, quiz in enumerate(self.quizzes, 1):
            print(f"[{idx}] {quiz.question}")

        prompt = f"\n삭제할 퀴즈 번호를 입력하세요 (1~{len(self.quizzes)}, 취소: 0): "
        choice = self.get_valid_input(prompt, 0, len(self.quizzes))

        if choice == 0:
            print("\n삭제를 취소했습니다.")
            return

        # 선택한 퀴즈 삭제 및 파일 영구 반영
        deleted_quiz = self.quizzes.pop(choice - 1)
        self.save_state()
        print(f"\n✅ '{deleted_quiz.question}' 문제가 삭제되었습니다. (state.json 반영 완료)")