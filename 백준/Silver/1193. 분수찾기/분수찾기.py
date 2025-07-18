x=int(input()) #주어진 숫자

# x=1 -> 1번째 줄
# x=2,3 -> 2번째 줄
# x=4,5,6 -> 3번째 줄
# x=7,8,9,10 -> 4번째 줄
# 몇번째 줄인지만 알면 분수를 구할 수 있다

def which_row(x): #몇번째 줄인지
    num=1
    while True:
        if (num-1)*num/2 < x <= num*(num+1)/2:
            break
        else:
            num+=1
    return num

# 홀수번째 줄일 땐 n/1 -> 1/n
# 짝수번째 줄일 땐 1/n -> n/1
row=which_row(x)
order= int(x - (row-1)*row/2) #그 줄 내에서 몇번째인지

a=b=0 #분모와 분자
if row%2!=0: #짝수번째 줄
    a=row-(order-1)
    b=order
else:
    a=order
    b=row-(order-1)
    
print(f"{a}/{b}")