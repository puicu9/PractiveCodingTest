#1차 시도 실패

# def solution(price, money, count):
#     answer = -1
#     total = 0
#
#     for i in range(count):
#         total += price * (i + 1)
#         # print (total)
#     answer = money - total
#     print("total", total)
#     print("answer : ", answer)
#
#     return answer if (answer > 0) else -answer;

#2차 시도 - 성공
# 원인 : return 값이 0 이상일 경우, 0으로 반환하라는 조건이 있었기 때문임.
def solution(price, money, count):
    answer = -1
    total = 0

    for i in range(count):
        total += price * (i + 1)
        # print (total)
    answer = money - total

    return 0 if (answer >= 0) else -answer;

# print(solution(3, 20,4))