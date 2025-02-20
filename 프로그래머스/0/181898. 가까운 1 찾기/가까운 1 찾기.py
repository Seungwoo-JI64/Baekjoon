def solution(arr, idx):
    if 1 in arr[idx:]:
        for i in range(idx, len(arr)):
            if arr[i]==1:
                return i
    else:
        return -1