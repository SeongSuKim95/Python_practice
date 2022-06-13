import math

def solution(w,h):    
    
    if w != h:
        g = math.gcd(w,h)
        w_g = w//g
        h_g = h//g

        slope = -h_g/w_g

        y = [int(slope*i + h_g) for i in range(0,w_g)]
        y_sum = sum(y[1:]) * 2 * g

        square = w * (h - h_g)
        return y_sum+square
    
    else :
        if w == 1:
            return 0
        else :
            
            return w*(w-1)