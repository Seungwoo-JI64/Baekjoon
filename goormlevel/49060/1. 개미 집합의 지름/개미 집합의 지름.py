n, d = map(int, input().split())
ant=list(map(int, input().split()))
ant.sort()
min_remove=9999999999 #제거하는 개미 수 - 최소 

right=0 #현재 기준 개미의 인덱스로부터 항상 오른쪽에 있어야함
for i in range(n): #현재 기준 개미 인덱스
	current_ant=ant[i]
	while right<n and ant[right]<=current_ant+d:
		right+=1 #해당 범위 이전까지의 최대 인덱스를 저장

	non_remove=right-i #범위 안에 있는 개미 수 -> 제거하지 않음
	if n-non_remove<min_remove:
		min_remove=n-non_remove
print(min_remove)