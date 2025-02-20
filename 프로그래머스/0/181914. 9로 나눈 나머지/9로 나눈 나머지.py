def solution(number):
    temp=0
    for i in number:
        temp+=int(i)
    return temp%9