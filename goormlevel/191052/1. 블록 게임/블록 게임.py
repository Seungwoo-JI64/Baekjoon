# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n=int(input())
arrow=list(str(input()))
score=list(map(int, input().split()))

blockmap={}
blockmap[(0,0)]=1 #초기 시작점
history=[]
history.append((0,0))

x=y=0 #최근 위치

for i in range(n):
	if arrow[i]=="R":
		x+=1
	elif arrow[i]=="L":
		x-=1
	elif arrow[i]=="U":
		y+=1
	elif arrow[i]=="D":
		y-=1

	while (x,y) in blockmap: #계속 마지막으로 놓은 것을 제거
		# if not recent_blocks: #제거할 블록이 더이상 없는 경우
		# 	break
			
		remove=history.pop()
		del blockmap[remove]

	blockmap[(x,y)]=score[i]
	history.append((x,y))

print(sum(blockmap.values()))