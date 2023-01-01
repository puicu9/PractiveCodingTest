def solution(s):
    answer = ''
    list = s.split(' ')
    print(list) #[u'try', u'hello', u'world']
    for i in list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
            #end if
        answer += ' '
    return answer[0:-1]

print(solution("try hello world"))