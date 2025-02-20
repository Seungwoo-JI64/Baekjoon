def solution(n):
    answer = [n]
    while n!=1:
        if n%2==0: #짝수
            n/=2
        else: #홀수
            n=3*n+1
        answer.append(n)
    return answer