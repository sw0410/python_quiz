import json

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
        pass

    def check_answer(self, user_input):
        """사용자가 입력한 번호(int)가 정답과 일치하는지 비교하여 True/False를 반환합니다."""
        # TODO 3: user_input과 self.answer가 같은지 비교한 결과(bool)를 return 하세요.
        pass


# === 동작 검증 구역 (Coin #1 손끝 피드백용) ===
if __name__ == "__main__":
    with open("state.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1번 문제 데이터로 Quiz 인스턴스 조립
    q1_data = data["quizzes"][0]
    q1 = Quiz(q1_data["question"], q1_data["choices"], q1_data["answer"])

    # 화면 출력 및 채점 기능 동작 검증
    q1.display()
    
    test_input = 2
    is_correct = q1.check_answer(test_input)
    print(f"\n[테스트 입력: {test_input}] -> 정답 여부: {is_correct}")