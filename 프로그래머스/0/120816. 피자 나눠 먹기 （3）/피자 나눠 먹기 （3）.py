def solution(slice, n):
    num=n%slice
    if num==0:
        answer=n//slice
    else:
        answer=n//slice+1
    return answer