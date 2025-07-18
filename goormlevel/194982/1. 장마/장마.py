N, M = map(int, input().split())
land_height = list(map(int, input().split()))  # 땅 높이를 정수형 리스트로 받음

# 각 날짜의 비 정보를 저장 (s, e)
# 문제에서 1번부터 N번 집이라고 했으므로, 0-indexed로 변환하여 저장
rain_events = []
for _ in range(M):
    s, e = map(int, input().split())
    rain_events.append((s - 1, e - 1)) # 0-indexed로 변환

rain_height = [0] * N  # 각 집에 현재 쌓여있는 물의 높이
# 각 집에 마지막으로 비가 내린 날짜 (0-indexed)
# -1로 초기화하여 아직 비가 내리지 않은 상태를 나타냄
last_rain_day = [-1] * N 

for day_idx in range(M): # 0부터 M-1까지 반복 (실제 날짜는 day_idx + 1)
    s, e = rain_events[day_idx]

    # 1. 비 내리기
    # 해당 구간의 집에 물 높이 1 증가
    # 그리고 해당 집에 마지막으로 비가 내린 날짜 업데이트
    for house_idx in range(s, e + 1):
        rain_height[house_idx] += 1
        last_rain_day[house_idx] = day_idx # 현재 날짜(0-indexed) 기록

    # 2. 배수 시스템 작동 (현재 날짜가 3의 배수일 때)
    # 실제 날짜는 day_idx + 1 이므로, (day_idx + 1) % 3 == 0 으로 확인
    if (day_idx + 1) % 3 == 0:
        for house_idx in range(N):
            # 배수 시스템은 현재 날짜 기준 2일 이내에 (즉, 오늘, 어제, 그제) 비가 내린 집에만 작동
            # last_rain_day[house_idx]가 -1이 아니며,
            # 현재 날짜(day_idx)에서 마지막 비 내린 날짜를 뺀 값이 2 이하면 조건 만족
            if last_rain_day[house_idx] != -1 and (day_idx - last_rain_day[house_idx]) <= 2:
                if rain_height[house_idx] > 0: # 물이 쌓여있어야 감소 가능
                    rain_height[house_idx] -= 1

# 3. 장마가 끝난 후, 최종 땅 높이 계산 및 출력
for i in range(N):
    land_height[i] += rain_height[i]
    print(land_height[i], end=" ")