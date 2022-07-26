def solution(n):
    
    k1 = 0
    k2 = 1 
    
    for i in range(n-1):
        temp1 = k1
        temp2 = k2
        k1 = temp2 % 1234567
        k2 = (temp1 + temp2) % 1234567
        
    return k2

# def solution(n):
    
#     k1 = 0
#     k2 = 1 
    
#     return fibonacci(k1,k2,n)

# def fibonacci(n1,n2,k):
#     if k == 0:
#         return n1 % 1234567
#     else :
#         k -=1
#         return fibonacci(n2,n1+n2,k) 
    
    