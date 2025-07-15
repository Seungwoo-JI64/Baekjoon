num=input()

# 314(8진수) -> 3 / 1 / 4(각각 10진수) -> 011, 001, 100 -> 11001100

result=[]
temp=[]
for n in num: #한자릿수씩 분해
    n=int(n) #10진수로 변환
    
    #10진수를 2진수로 변환 (3비트)
    bit=[]
    for _ in range(3):
        bit.append(str(n%2))
        n=n//2
    temp.append("".join(bit[::-1])) #각 비트를 합치기
    
result=int("".join(temp)) #각 3비트를 통합하기
print(result)