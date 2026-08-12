import sys

# ==========================================
# 1. Quiz 클래스 (개별 퀴즈 표현)
# ==========================================
class Quiz:
    """개별 퀴즈를 표현하는 클래스"""

    def __init__(self, question: str, choices: list[str], answer: int):
        self.question = question
        self.choices = choices  # 4개의 선택지 리스트
        self.answer = answer    # 정답 번호 (1~4)

    def is_correct(self, user_choice: int) -> bool:
        """사용자가 입력한 번호가 정답인지 검증"""
        return self.answer == user_choice

    def to_dict(self) -> dict:
        """state.json 저장을 위한 직렬화"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Quiz':
        """json 데이터로부터 객체를 복원하는 팩토리 메서드"""
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"]
        )


# 기본 퀴즈 데이터셋 (최소 5개)
DEFAULT_QUIZZES = [
    Quiz("Python에서 가변(Mutable) 객체에 해당하는 것은?", ["tuple", "int", "list", "str"], 3),
    Quiz("Python에서 리스트의 길이를 반환하는 함수는?", ["size()", "len()", "length()", "count()"], 2),
    Quiz("다음 중 Python의 주석 기호로 올바른 것은?", ["//", "/* */", "#", "--"], 3),
    Quiz("딕셔너리(dict)에서 키-값 쌍을 모두 가져오는 메서드는?", ["keys()", "values()", "items()", "get()"], 3),
    Quiz("Python의 붕어빵 틀에 해당하는 개념으로, 객체를 생성하기 위한 설계도는?", ["Function", "Class", "Module", "Package"], 2)
]


# ==========================================
# 2. QuizGame 클래스 (전체 게임 제어 및 관리)
# ==========================================
class QuizGame:
    """게임 전체 흐름, 상태 관리 및 인터페이스를 총괄하는 클래스"""

    def __init__(self):
        self.quizzes: list[Quiz] = list(DEFAULT_QUIZZES)  # 기본 퀴즈 데이터 탑재
        self.best_score: int = 0

    def display_menu(self):
        """메인 메뉴 출력"""
        print("\n" + "=" * 30)
        print("       PYTHON QUIZ GAME")
        print("=" * 30)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")
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
                    self.show_best_score()
                elif choice == 5:
                    print("\n게임을 종료합니다. 이용해 주셔서 감사합니다!")
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 프로그램이 강제 종료 요청을 받았습니다.")
            print("안전하게 프로그램을 종료합니다.")
            sys.exit(0)

    def play_quiz(self):
        """1. 퀴즈 풀기 기능 구현"""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        print("\n" + "=" * 30)
        print("         퀴즈 풀기 시작")
        print("=" * 30)

        current_score = 0
        total_quizzes = len(self.quizzes)

        for idx, quiz in enumerate(self.quizzes, 1):
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
        else:
            print(f"현재 최고 점수: {self.best_score}점")
        print("=" * 30)

    def add_quiz(self):
        print("\n[안내] 퀴즈 추가 기능은 준비 중입니다.")

    def show_quiz_list(self):
        print("\n[안내] 퀴즈 목록 기능은 준비 중입니다.")

    def show_best_score(self):
        print("\n[안내] 최고 점수 확인 기능은 준비 중입니다.")