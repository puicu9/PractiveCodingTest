# 문제 설명
#
# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

import numpy as np
def solution(arr1, arr2):
    answer = [[]]
    answer = np.add(arr1, arr2)
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
# [[4,6],[7,9]]


arr3 = [[1],[2]]
arr4 = [[3],[4]]
# [[4],[6]]

print(solution(arr1, arr2))
print('-' * 40)
print(solution(arr3, arr4))


def solution1(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]

    return arr1
print('-' * 40)
print(solution1(arr1, arr2))
print('-' * 40)
print(solution1(arr3, arr4))
