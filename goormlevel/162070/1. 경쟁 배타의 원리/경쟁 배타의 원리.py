# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n,k=map(int, input().split())
teritory=[[0]*1001 for _ in range(1001)] #1000x1000의 공간, 값은 종의 개수

for _ in range(n):
	x1,y1,x2,y2=map(int, input().split()) #좌표
	#각 영역의 꼭짓점 좌표에 표시를 한다
	teritory[y1][x1]+=1
	teritory[y1][x2]-=1
	teritory[y2][x1]-=1
	teritory[y2][x2]+=1

#이후 행, 열방향 누적합을 실행
#누적합이 k인것만 찾으면 된다
for i in range(1001):
	for j in range(1,1001):
		teritory[i][j]+=teritory[i][j-1]
for j in range(1001):
	for i in range(1,1001):
		teritory[i][j]+=teritory[i-1][j]

count=0
for i in range(1000):
	for j in range(1000):
		if teritory[i][j]==k:
			count+=1
print(count)