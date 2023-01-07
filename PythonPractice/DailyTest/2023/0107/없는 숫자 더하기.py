def solution(numbers):
    total = 0
    minus = 0
    for i in range(10):
        total += i
    for j in numbers:
        minus += j

    return total-minus