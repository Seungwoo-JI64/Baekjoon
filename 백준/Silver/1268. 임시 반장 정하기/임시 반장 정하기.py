n=int(input())
temp=[]
for _ in range(n):
    temp.append(list(map(int, input().split())))

result_count=-1 #학생 카운트
result_index=-2 #학생 인덱스

for i in range(n): #학생
    count=set() #한번이라도 같은반이여야 하므로 중복은 제거해야한다
    for j in range(5): #학년
        for k in range(n):
            if i==k: #해당 학생 제외했을 때
                continue
            if temp[i][j]==temp[k][j]:
                count.add(k) #해당 학생 추가
    if result_count<len(count): #중복일 경우 가장 작은 번호만
        result_count=len(count)
        result_index=i
print(result_index+1)
            