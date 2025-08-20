def solution(s):
    answer = ''
    s=s.lower() #모두 소문자
    for i in range(len(s)):
        if i==0 or s[i-1]==" ": #첫 문자 또는 각 단어의 첫 문자
            if s[i].isalpha(): #알파벳이면
                answer+=s[i].upper()
            else:
                answer+=s[i]
        else:
            answer+=s[i]
                
    return answer