def solution(num_list):
    answer = 0
    odd=0
    even=0
    for i in range(len(num_list)):
        if i%2!=0:
            odd+=num_list[i]
        else:
            even+=num_list[i]
    answer=(odd if odd>even else even)
    return answer