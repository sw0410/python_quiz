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


# 기본 퀴즈 데이터셋
DEFAULT_QUIZZES = [
    Quiz("Python에서 가변(Mutable) 객체에 해당하는 것은?", ["tuple", "int", "list", "str"], 3),
    Quiz("Python에서 리스트의 길이를 반환하는 함수는?", ["size()", "len()", "length()", "count()"], 2),
    Quiz("다음 중 Python의 주석 기호로 올바른 것은?", ["//", "/* */", "#", "--"], 3),
    Quiz("딕셔너리(dict)에서 키-값 쌍을 모두 가져오는 메서드는?", ["keys()", "values()", "items()", "get()"], 3),
    Quiz("Python의 붕어빵 틀에 해당하는 개념으로, 객체를 생성하기 위한 설계도는?", ["Function", "Class", "Module", "Package"], 2)
]