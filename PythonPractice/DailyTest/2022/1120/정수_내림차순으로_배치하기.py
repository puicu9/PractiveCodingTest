# 문제 설명
# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    answer = ''.join(answer)
    return int(answer)
print(solution(118372))

print('-' * 40)

def second_solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)
    total = ''
    for i in answer[0::]:
        total += i
    return total
print(second_solution(118372))




