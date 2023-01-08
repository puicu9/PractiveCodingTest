def solution(a, b):
    total = 0  # 총합
    n = len(a)
    # print(n)

    for i in range(n):
        total += a[i] * b[i]

    return total