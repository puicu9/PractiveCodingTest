# 출처 : 프로그래머스 https://school.programmers.co.kr/

# 코드실행은 문제 없으나, 정답률 25%로 패스 못하고 있음.

def solution(survey, choices):
    answer = ''
    su = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0, }
    print(survey)
    print(choices)
    print('-' * 40)

    for i in range(len(survey)):
        leftChar = str(survey[i][0])
        rightChar = str(survey[i][1])
        print('firIdx : ', leftChar)
        print('secIdx : ', rightChar)

        num = choices[i]
        print('num : ', num)

        if num < 4:
            print('오른쪽에 더하기')
            su[leftChar] += int(num)
        if num > 4:
            print('왼쪽에 더하기')
            su[rightChar] += int(num)
        #End if
        print('-' * 40)
    #End for
    answer += "R" if su["R"] >= su["T"] else "T"
    answer += "C" if su["C"] >= su["F"] else "F"
    answer += "J" if su["J"] >= su["M"] else "M"
    answer += "A" if su["A"] >= su["N"] else "N"
    print(su)

    return answer
# 어피치형(A) - 비동의, 네오형(N) - 동의
# 약간 동의 A
# 매우 비동의 N
# 위 예시처럼 네오형이 비동의, 어피치형이 동의인 경우만 주어지지 않고,
# 질문에 따라 네오형이 동의, 어피치형이 비동의인 경우도 주어질 수 있습니다.
testSurvey01 = ["AN", "CF", "MJ", "RT", "NA"]
TestChoices01 = [5, 3, 2, 7, 5]

testSurvey02 = ["TR", "RT", "TR"]
TestChoices02 = [7, 1, 3]

testSurvey03 = ["RT", "TR", "CF", "FC", "JM", "MJ", "AN", "NA"]
TestChoices03 = [7,     1,    3,    3,    6,    4,    3,    1]
# T : 7 + 1, C : 3, F:3, J :  , M :6,  A :3, N : 1
# T 8, C 3, J 0, M 6, A 3, N : 1
# TCMA

print(solution(testSurvey01, TestChoices01))
print('정답은 TCMA로 나와야함')

print('-' * 50)
print(solution(testSurvey02, TestChoices02))
print('정답 : RCJA')

print('-' * 50)
print(solution(testSurvey03, TestChoices03))
print('정답 : TCJA')
