def solution(s, n):
    answer = ''
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

# chr(숫자) : 숫자에 맞는 아스키 코드를 반환한다.
# ord(문자) : 아스키 코드를 반환해준다.
# 만약 ord(c) + n이 'z'를 넘어갈 경우 총 알파벳 갯수를 빼줘서 다시 'a'부터 시작하도록 했다.
