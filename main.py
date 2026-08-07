# 가장 작은 전체 과업을 담은 딕셔너리 중심(Center)
# q = {
#     "prompt" : "노르웨이의 수도는?",
#     "options" : ["1. 오슬로","2. 트롬쇠","3. 릴해머","4. 베르겐"],
#     "answer" : 1
# }

# # 2. 화면 출력 (Perception)
# print (q["prompt"])

# for i in q["options"]:
#     print(i)


# # 3. 입력 및 정답 판별 (Feedback Loop Center)

# user_input = int(input("번호를 입력하세요"))

# if user_input == q["answer"]:
#     print("⭕ 정답입니다.")
# else:
#     print("❌ 오답입니다.")

# ==================================================
# 기존 딕셔너리를 Question 클래스 객체(q1)로 전환
# ==================================================




# class Question:
#     def __init__(self, prompt, options, answer):
#        self.prompt = prompt
#        self.options = options
#        self.answer = answer 
#     def check_answer(self, user_input):
#         return user_input == self.answer
            
# q1 = Question(
#     prompt="노르웨이의 수도는?",
#     options=["1. 오슬로", "2. 트롬쇠", "3. 릴해머", "4. 베르겐"],
#     answer=1
# )

# # 2. 화면 출력
# print(q1.prompt)
# for i in q1.options:
#     print(i)


# # # 3. 입력 및 정답 판별 (클래스의 메서드 호출)

# user_input = int(input("번호를 입력해주세요:"))

# if q1.check_answer(user_input):
#     print("⭕ 정답입니다.")
# else:
#     print("❌ 오답입니다.")


# import json

# with open("state.json", "r", encoding="utf-8") as f:
#     q_data = json.load(f)

# q1 = Question(
#     prompt=q_data["prompt"],
#     options=q_data["options"],
#     answer=q_data["answer"]
# )

# Coin 3 
# import json

# # 1. 클래스 정의 (유전자)
# class Question:
#     def __init__(self, prompt, options, answer):
#         self.prompt = prompt
#         self.options = options
#         self.answer = answer

#     def check_answer(self, user_inpu햐t):
#         return user_input == self.answer


# # 2. 바깥 파일(state.json)에서 데이터 불러오기
# with open("state.json", "r", encoding="utf-8") as f:
#     q_data = json.load(f)

# # 3. 전체 타이틀 출력
#     print(f"=== {q_data['title']} ===")

# # 3. 읽어온 데이터로 객체 조립
# q1 = Question(
#     prompt=q_data["prompt"],
#     options=q_data["options"],
#     answer=q_data["answer"]
# )

# # 4. 화면 출력
# print(q1.prompt)
# for i in q1.options:
#     print(i)

# # 5. 입력 및 채점
# user_input = int(input("\n번호를 입력해주세요: "))

# if q1.check_answer(user_input):
#     print("⭕ 정답입니다!")
# else:
#     print("❌ 오답입니다.")





import json

# 1. 설계도 (Question 클래스)
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def check_answer(self, user_input):
        return user_input == self.answer


# 2. 바깥 데이터 읽어오기
with open("state.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 3. 전체 타이틀 출력
print(f"=== {data['title']} ===\n")

# 3. [Coin #5] 점수 집계를 위한 상태 변수 선언
score = 0
total_questions = len(data["questions"])

# 4. [Coin #4] data["questions"]의 문제들을 순서대로 꺼내어 조립 및 출제
for q_data in data["questions"]:
    # 💡 작성하셨던 객체 조립 구문이 for 문 안으로 들어옵니다
    q = Question(
        prompt=q_data["prompt"],
        options=q_data["options"],
        answer=q_data["answer"]
    )

    print(q.prompt)
    for option in q.options:
        print(option)

    # user_input = int(input("\n번호를 입력해주세요: "))

    # if q.check_answer(user_input):
    #     print("⭕ 정답입니다.\n")
    #     # [Coin #5] 정답일 때만 점수 1 증가
    #     score += 1

    # else:
    #     print("❌ 오답입니다.\n")

# [Coin #6 핵심] 숫자가 입력될 때까지 안전하게 반복 받는 울타리
    while True:
        try:
            user_input = int(input("\n번호를 입력해주세요: "))
            break  # 올바른 숫자가 입력되면 안전하게 반복문 탈출
        except ValueError:
            print("⚠️ 숫자로 된 번호만 입력해 주세요. (예: 1, 2)")

    if q.check_answer(user_input):
        print("⭕ 정답입니다.\n")
        score += 1
    else:
        correct_option = q.options[q.answer - 1]
        print(f"❌ 틀렸습니다. (정답: {correct_option})\n")

print("=" * 30)
print(f"🎉 퀴즈 종료! 최종 점수: {score} / {total_questions}")
print("=" * 30)




    