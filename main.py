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


import json

# 1. 클래스 정의 (유전자)
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def check_answer(self, user_inpu햐t):
        return user_input == self.answer


# 2. 바깥 파일(state.json)에서 데이터 불러오기
with open("state.json", "r", encoding="utf-8") as f:
    q_data = json.load(f)

# 3. 읽어온 데이터로 객체 조립
q1 = Question(
    prompt=q_data["prompt"],
    options=q_data["options"],
    answer=q_data["answer"]
)

# 4. 화면 출력
print(q1.prompt)
for i in q1.options:
    print(i)

# 5. 입력 및 채점
user_input = int(input("\n번호를 입력해주세요: "))

if q1.check_answer(user_input):
    print("⭕ 정답입니다!")
else:
    print("❌ 오답입니다.")




    