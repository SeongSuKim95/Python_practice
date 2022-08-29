def solution(A,B):
    
    A1 = sorted(A)
    B1 = sorted(B,reverse=True)
    A2 = A1[::-1]
    B2 = B1[::-1]
    temp1 , temp2 = 0,0
    for a1,b1,a2,b2 in zip(A1,B1,A2,B2):
        temp1 += a1*b1
        temp2 += a2*b2

    return min(temp1,temp2)