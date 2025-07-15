num=int(input())
ppl_list=list(input() for _ in range(num))
count=[]

first_list=list(str(name)[0] for name in ppl_list) #성의 첫글자만

for i in first_list:
    if first_list.count(i)>=5:
        count.append(i)
count=set(count) #중복 제거

if count:
    print("".join(sorted(count)))
else:
    print("PREDAJA")
