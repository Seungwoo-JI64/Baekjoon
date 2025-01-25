def solution(n):
    answer=0
    for a in range(1,n+1):
        if (n/a).is_integer():
            answer+=1
    return answer