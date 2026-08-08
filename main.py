import json
import sys  # 1. 외부 모듈 불러오기 모음

# 2. 공통 입력 방파제 함수 (Coin #2)
def get_safe_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            raw_input = input(prompt).strip()

            # TODO 1: raw_input이 빈 문자열("")이면 경고 메시지 출력 후 continue
            # ------------------------------------------------------------------------
            if raw_input == "":
                print("⚠️ 빈 값은 입력할 수 없습니다.")
                continue
            # ------------------------------------------------------------------------

            value = int(raw_input)

            # TODO 2: value가 min_val 미만이거나 max_val 초과인지 검증 후 continue
            # 힌트: (min_val is not None and value < min_val) 조건 활용
            # ------------------------------------------------------------------------
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"⚠️ {min_val}~{max_val} 사이의 숫자를 입력해 주세요.")
                continue
            # ------------------------------------------------------------------------

            return value

        except ValueError:
            print("⚠️ 숫자로 된 번호만 입력해 주세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n\n👋 프로그램을 안전하게 종료합니다.")
            sys.exit(0)

# =========================================================
# [Coin #3] state.json 상태 읽기 및 저장 함수
# =========================================================
def load_state(filepath="state.json"):
    """state.json 파일에서 title, quiz 객체 리스트, best_score를 읽어옵니다."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 💡 [핵심 수리] title 변수를 선언하고 JSON 데이터에서 불러옵니다.
        title = data.get("title", "세계 지리 상식 퀴즈")
        best_score = data.get("best_score", 0)

        quizzes = []
        for q in data.get("questions", []):
            quizzes.append(Quiz(q["question"], q["choices"], q["answer"]))

        # 이제 title 변수가 존재하므로 NameError 없이 정상 반환됩니다.
        return title, quizzes, best_score

    except FileNotFoundError:
        print("⚠️ state.json 파일을 찾을 수 없어 기본 설정으로 시작합니다.")
        return "기본 퀴즈", [], 0


def save_state(title, quizzes, best_score, filepath="state.json"):
    """Quiz 객체 리스트와 최고 점수를 state.json 파일에 저장합니다."""
    # Quiz 객체들을 딕셔너리 형태의 리스트로 변환
    quiz_dicts = []
    for q in quizzes:
        # TODO 2: q.question, q.choices, q.answer를 딕셔너리 형태로 만들어 quiz_dicts에 append 하세요.
        # 힌트: {"question": q.question, "choices": q.choices, "answer": q.answer}
        # ------------------------------------------------------------------------
        quiz_dicts.append({"question": q.question,"choices": q.choices, "answer": q.answer})
        # ------------------------------------------------------------------------
        pass

    data = {
        "quizzes": quiz_dicts,
        "best_score": best_score
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# =========================================================
# [Coin #1] 기존에 작성하여 검증을 마친 Quiz 클래스 (유지!)
# =========================================================
class Quiz:
    def __init__(self, question, choices, answer):
        # TODO 1: 전달받은 매개변수(question, choices, answer)를 인스턴스 변수(self.xxx)에 저장하세요.
        self.question = question
        self.choices = choices
        self.answer = answer
        pass

    def display(self):
        """퀴즈 문제와 4개 선택지를 화면에 출력합니다."""
        # TODO 2: self.question과 self.choices를 활용해 문제와 보기(for문 사용)를 출력하세요.
        print(f"\nQ. {self.question}")

        for choice in self.choices:
            print(f"{choice}")
        pass

    def check_answer(self, user_input):
        """사용자가 입력한 번호(int)가 정답과 일치하는지 비교하여 True/False를 반환합니다."""
        # TODO 3: user_input과 self.answer가 같은지 비교한 결과(bool)를 return 하세요.
        return user_input == self.answer
        pass

# === 동작 검증 구역 (Coin #3 테스트) ===
if __name__ == "__main__":

    # 1. state.json에서 데이터 불러오기
    title, quizzes, best_score = load_state()

    print(f"=== [{title}] ===")
    print(f"✅ 불러온 퀴즈 개수: {len(quizzes)}개")
    print(f"🏆 최고 점수: {best_score}점\n")
    
    
    # 2. 첫 번째 퀴즈 화면 출력 테스트
    if quizzes:
        quizzes[0].display()

    # 3. 데이터 저장 테스트
    save_state(title, quizzes, best_score)
    print("\n✅ state.json 파일에 성공적으로 저장되었습니다.")


# =========================================================
# [Coin #4] 퀴즈 풀기 엔진 함수
# =========================================================
def play_quiz(quizzes, best_score):
    """퀴즈를 순서대로 출제하고 점수를 집계하여 (현재 점수, 갱신된 최고 점수)를 반환합니다."""
    if not quizzes:
        print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요!")
        return 0, best_score

    print("\n==========================================")
    print("🚀 퀴즈 풀기를 시작합니다!")
    print("==========================================")

    current_score = 0
    total_quizzes = len(quizzes)

    for idx, quiz in enumerate(quizzes, 1):
        print(f"\n[문제 {idx} / {total_quizzes}]")
        # 1. 퀴즈 문제와 보기 출력
        quiz.display()

        # TODO 1: get_safe_input 함수를 호출하여 1부터 len(quiz.choices) 사이의 안전한 번호를 입력받으세요.
        # ------------------------------------------------------------------------
        user_input = get_safe_input("정답 번호를 입력하세요: ", min_val=1, max_val=len(quiz.choices))
        # ------------------------------------------------------------------------

        # TODO 2: quiz.check_answer(user_input)으로 정답을 확인하고,
        #         정답이면 current_score를 1 증가시키고 "⭕ 정답입니다!" 출력,
        #         오답이면 "❌ 틀렸습니다! 정답은 N번입니다." 출력하세요.
        # ------------------------------------------------------------------------
        if quiz.check_answer(user_input):
            print("⭕ 정답입니다!")
            current_score += 1
        else:
            print(f"❌ 틀렸습니다! 정답은 {quiz.answer}번입니다.")
        # ------------------------------------------------------------------------

    print("\n==========================================")
    print(f"🎉 퀴즈 종료! 나의 점수: {current_score} / {total_quizzes}")

    # 최고 점수 갱신 확인
    if current_score > best_score:
        print(f"🎊 축하합니다! 새로운 최고 점수 달성! ({best_score}점 ➔ {current_score}점)")
        best_score = current_score
    else:
        print(f"🏆 현재 최고 점수: {best_score}점")

        return current_score, best_score