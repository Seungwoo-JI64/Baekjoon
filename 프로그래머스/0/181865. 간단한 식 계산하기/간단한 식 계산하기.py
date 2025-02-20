def solution(binomial):
    answer = 0
    temp=binomial.split()
    a=int(temp[0])
    b=int(temp[2])
    op=temp[1]
    
    if op=="+":
        answer=a+b
    elif op=="-":
        answer=a-b
    else:
        answer=a*b
    return answer