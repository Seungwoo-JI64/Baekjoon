def solution(X, Y):
    answer=''
    temp=sorted(list(set(X)&set(Y)),reverse=True)
    if len(temp)==0:
        answer="-1"
    elif temp==["0"]:
        answer="0"
    else:
        for i in temp: #temp는 내림차순정렬
            answer+=i*min(X.count(i),Y.count(i))
    return answer
        