import sys
from quiz import Quiz, DEFAULT_QUIZZES

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
        """
        공통 입력 검증 메서드:
        - 공백 제거 후 처리
        - 숫자 변환 실패 / 범위 밖 입력 / 빈 입력 시 안내 메시지 후 재입력
        """
        while True:
            try:
                user_input = input(prompt).strip()

                # 빈 입력 처리
                if not user_input:
                    print("⚠️ 입력이 비어 있습니다. 다시 입력해 주세요.")
                    continue

                # 숫자 변환
                choice = int(user_input)

                # 범위 검증
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
            # Ctrl+C 또는 입력 스트림 종료 시 비정상 종료 방지
            print("\n\n⚠️ 프로그램이 강제 종료 요청을 받았습니다.")
            print("안전하게 프로그램을 종료합니다.")
            sys.exit(0)

    # --- 각 메뉴의 스텁(Stub) 메서드 ---
    def play_quiz(self):
        print("\n[안내] 퀴즈 풀기 기능은 준비 중입니다.")

    def add_quiz(self):
        print("\n[안내] 퀴즈 추가 기능은 준비 중입니다.")

    def show_quiz_list(self):
        print("\n[안내] 퀴즈 목록 기능은 준비 중입니다.")

    def show_best_score(self):
        print("\n[안내] 최고 점수 확인 기능은 준비 중입니다.")