# https://school.programmers.co.kr/learn/courses/30/lessons/12916?language=python3

def solution(s):
    answer = True

    str = s.upper()
    strP = []
    strY = []

    for i in range(len(str)):
        if str[i] == 'P':
            strP.append(i)
        elif str[i] == 'Y':
            strY.append(i)

    if len(strP) != len(strY):
        answer = False

    return answer

print(solution("pPoooyY"))
print(solution("Pyy"))
