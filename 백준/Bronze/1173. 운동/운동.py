N, m, M, T, R = map(int, input().split())
current = m #현재 심박수
cnt = 0 #현재 운동횟수
total = 0 #총 운동횟수

if m+T>M: #운동을 시작도 못할 때
    print(-1)
else: #운동 시작
    while cnt < N: #운동 N회
        if current + T <= M: #운동 할 수 있음
            cnt+=1
            current+=T
        else: #운동 할 수 없음
            current = max(m, current-R) #최소심박수와 휴식중 택1
        total+=1
        
    print(total)
            
    