def solution(num_list):
    answer = 0
    a=[]
    for i in range(len(num_list)):
        if num_list[i]<0:
            a.append(i)
    if a==[]:
        answer=-1
    else:
        answer=min(a)
    return answer