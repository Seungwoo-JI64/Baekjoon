# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N=int(input())

#패턴 000 100 010 001 101 총 5가지
dp=[[0]*5 for _ in range(N)] #dp는 각각의 패턴에 대해 경우의 수를 저장한다

#전이 맵, key : 현재, value : 이전에 가능한 경우
transition_map={
	0:[0,1,2,3,4],
	1:[0,2,3],
	2:[0,1,3,4],
	3:[0,1,2],
	4:[0,2]
}

for j in range(5): #첫번째 줄 각각의 패턴에 대해 한가지 경우의 수
	dp[0][j]=1
	
for i in range(1,N): #두번째 줄부터
	for now in range(5): #현재 무슨 패턴인가
		for prev in transition_map[now]: #현재 패턴에 가능한 과거의 패턴은 무엇인가
			dp[i][now]=(dp[i][now]+dp[i-1][prev])%100000007 #이전 패턴(과거엔 현재였음)의 경우의 수를 더하기

sum=0
for j in range(5): #모든 패턴의 합 구하기
	sum+=dp[N-1][j] #마지막줄
sum=sum%100000007
print(sum)