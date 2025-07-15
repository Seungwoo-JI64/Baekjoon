s1, s2, s3 = map(int, input().split())

num1=[num for num in range(1,s1+1)]
num2=[num for num in range(1,s2+1)]
num3=[num for num in range(1,s3+1)]

total=[]
for i in num1:
    for j in num2:
        for k in num3:
            total.append(i+j+k)
temp_list=list(set(total))

max_prep=0
result=0
for i in temp_list:
    if total.count(i) > max_prep:
        max_prep=total.count(i)
        result=i
print(result)
