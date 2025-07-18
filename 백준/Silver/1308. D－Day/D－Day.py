from datetime import datetime
y1, m1, d1=map(int, input().split()) #오늘 날짜
y2, m2, d2=map(int, input().split()) #캠프가 끝나는 날짜

if y1+1000<y2 or ((y1+1000==y2) and ((m1, d1)<=(m2, d2))): #천년 뒤에 끝날 때
    print("gg")
else:
    time=(datetime(y2,m2,d2)-datetime(y1,m1,d1)).days
    print(f"D-{time}")