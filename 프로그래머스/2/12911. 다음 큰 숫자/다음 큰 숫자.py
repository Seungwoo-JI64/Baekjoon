def solution(n):
    count_n=bin(n).count("1")
    answer=n
    while True:
        answer+=1
        if bin(answer).count("1")==count_n:
            break
        
    return answer