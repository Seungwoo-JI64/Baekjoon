def solution(myString, pat):
    temp=""
    for char in myString:
        if char=="B":
            temp+="A"
        else:
            temp+="B"
    if pat in temp:
        answer=1
    else:
        answer=0
    return answer