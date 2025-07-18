n=int(input())
text=[str(input()) for _ in range(n)]
text=list(set(text)) #중복 제거

text.sort() #알파벳순
text.sort(key=len) #길이순
for i in text:
    print(i)
