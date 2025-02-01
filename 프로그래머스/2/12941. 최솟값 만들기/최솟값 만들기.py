def solution(A,B):
    A.sort(reverse=True)           
    B.sort()                        
    sum = 0
    for i in range(len(A)):         
        sum += A.pop() * B.pop()       
    return sum