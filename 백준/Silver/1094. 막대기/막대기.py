temp=int(input()) #만들고자 하는 막대 길이
#23 = 64->32->16+8->16+4+2->16+4+2+1
a=0 #막대 개수
while temp!=0 :
    if temp==64:
        temp-=64
        a+=1
    elif 32<=temp<64:
        temp-=32
        a+=1
    elif 16<=temp<32:
        temp-=16
        a+=1
    elif 8<=temp<16:
        temp-=8
        a+=1
    elif 4<=temp<8:
        temp-=4
        a+=1
    elif 2<=temp<4:
        temp-=2
        a+=1
    else:
        temp-=1
        a+=1
print(a)
