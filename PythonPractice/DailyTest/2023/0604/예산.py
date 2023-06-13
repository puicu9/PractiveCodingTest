def solution(d, budget):
    d.sort()
    answer = 0
    add=0
    for i in range(len(d)):
        add+=d[i]
        if add <= budget:
            answer += 1
    return answer



#[1,3,2,5,4]	9	3
#[2,2,3,3]	10	4