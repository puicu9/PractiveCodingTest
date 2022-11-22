# 내 풀이
# def solution(s):
#     answer = ''
#
#     halfValue = int(len(s) / 2)
#     print(halfValue)
#
#     if len(s) % 2 == 0:
#         answer = s[halfValue-1:halfValue +1]
#     elif len(s) % 2 == 1:
#         answer = s[halfValue:halfValue +1]
#
#     return answer

# 다른 사람 풀이
def solution(s):
    if len(s) % 2 == 1:
        answer = s[len(s) // 2]
    else:
        answer = s[len(s) // 2 - 1:len(s) // 2 + 1]
    return answer

print(solution("abcde")) # c
print('-'* 40)
print(solution("qwer")) # we
print('-'* 40)
print(solution("qwerabc")) # r 나와야함
