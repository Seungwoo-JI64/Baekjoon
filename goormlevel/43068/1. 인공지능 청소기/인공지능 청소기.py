# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
time=int(input())
for _ in range(time):
	x, y, n = map(int, input().split())
	sum_xy=abs(x)+abs(y)
	if (n>=sum_xy) and ((n-sum_xy)%2==0):
		print("YES")
	else:
		print("NO")
	