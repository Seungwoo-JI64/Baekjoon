def solution(myString):
    answer = ''
    # temp=sorted(myString+"l")
    # idx=temp.index("l") #l의 위치 인덱스
    # for i in range(len(myString)):
    #     if myString[i] in temp[:idx]:
    #         answer+="l"
    #     else:
    #         answer+=myString[i]
    #시간초과
    for i in myString:
        if i<"l":
            answer+="l"
        else:
            answer+=i
    return answer