num=int(input())

temp=list(map(int, input().split()))

max_t=max(temp)
min_t=min(temp)

print(min_t*max_t)