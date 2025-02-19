def solution(arr):
    for i in range(len(arr)):
        if arr[i]%2==0 and arr[i]>=50:
            arr[i]=int(arr[i]/2)
        elif arr[i]%2!=0 and arr[i]<50:
            arr[i]=arr[i]*2
    answer=arr
    return answer