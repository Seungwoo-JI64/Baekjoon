def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp=0
        a=i
        while True:
            temp+=a
            a+=1
            if temp>n:
                break
            if temp==n:
                answer+=1
                break
    return answer