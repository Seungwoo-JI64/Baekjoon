big=int(input())
small=int(input())

temp=big-(big%100)
for i in range(temp, temp+100):
    if i%small==0:
        print(str(i)[-2:])
        break