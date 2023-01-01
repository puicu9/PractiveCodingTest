def solution(n):
    answer = 0
    for idx in range(1,n):
        if n % idx == 1:
            answer = idx
            break

    return answer


print(solution(10))
print(solution(12))