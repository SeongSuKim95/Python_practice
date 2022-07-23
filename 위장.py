import math
from itertools import combinations

def solution(clothes):
    answer = 0
    cloth_dict = {}
    for cloth in clothes :
        if cloth[1] not in cloth_dict.keys():
            cloth_dict[cloth[1]] = 1
        cloth_dict[cloth[1]] += 1
    
    return eval('*'.join([str(n) for n in list(cloth_dict.values())])) - 1

# 정석 풀이
# def solution(clothes):
#     clothes_type = {}

#     for c, t in clothes:
#         if t not in clothes_type:
#             clothes_type[t] = 2
#         else:
#             clothes_type[t] += 1

#     cnt = 1
#     for num in clothes_type.values():
#         cnt *= num

#     return cnt - 1
