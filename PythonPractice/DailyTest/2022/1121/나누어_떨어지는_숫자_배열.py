# 출처 : 프로그래머스 https://school.programmers.co.kr/

# 문제 설명
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.
#
# 제한사항
# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.

def solution(arr, divisor):
    answer = []
    print('arr : ', arr)
    print('divisor : ', divisor)


    for i in range(len(arr)):
        value = arr[i] % divisor
        print('value : ', value)

        if value == 0:
            answer.append(arr[i])
    if(len(answer) == 0):
        answer = [-1]

    return sorted(answer)

# answer.sort() 를 사용했을 땐 None값으로 반환돼 애먹음.
# 이에 대한 대안으로 sorted(answer)를 사용함.




test01arr =[5, 9, 7, 10]
test01divisor = 5

test02arr = [2, 36, 1, 3]
test02divisor = 1

test03arr = [3, 2, 6]
test03divisor = 10

# print('test01')
# print(solution(test01arr, test01divisor))
# print('-' * 50)
print('test02')
print(solution(test02arr, test02divisor))
# print('test03')
# print('-' * 50)
print(solution(test03arr, test03divisor))