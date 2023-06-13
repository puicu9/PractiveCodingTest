#풀이1
def solution(left, right):
    answer = 0
    lists = []

    # for, range로 범위 넣기
    for i in range(left, right + 1):
        lists.append(i)
    # print(lists) # 	[13, 14, 15, 16, 17], [24, 25, 26, 27]

    for j in lists:  # j : 배열 안의 숫자
        count = []  # 약수의 개수
        # print(j) # 배열 안 숫자 : 13 ~ 17
        for k in range(1, j + 1):  # k는 1부터 j까지의 숫자 나열
            if (j) % k == 0:
                count.append(k)
        print(len(count))  # 약수 개수 : 2, 4, 4, 5, 2 // 8, 3, 4, 4

        if len(count) % 2 == 0:  # 약수 개수가 짝수면
            answer += j
        else:
            answer -= j

    return answer


# 풀이2
def solution2(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer