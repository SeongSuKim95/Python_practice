import sys
from itertools import permutations
from collections import deque

N = int(input())
# num = list(map(int, input().split()))
seq = list(map(int,input().split()))

cal = ['+','-','*','//']
cal_input = list(map(int,input().split()))

cal_list = []
for i in range(4):
    if cal_input[i] == 0 :
        pass
    else :
        for j in range(cal_input[i]):
            cal_list.append(cal[i])

# print(cal_list)

# add, sub, mul, div = map(int,input().split())

max_value = -1e9
min_value = 1e9

num_case = list(permutations(cal_list,len(cal_list)))
q = deque(num_case)
# 가능한 배열 수
while q :
    cur_list = q.popleft()
    result = seq[0]
    for i in range(1,len(seq)):
        if cur_list[i-1] == "+":
            result += seq[i]
        elif cur_list[i-1] == "-":
            result -= seq[i]
        elif cur_list[i-1] == "*":
            result *= seq[i]
        else :
            if result < 0 :
                result = -(abs(result)//seq[i])
            else:
                result = result // seq[i]
    max_value = max(max_value,result)
    min_value = min(min_value,result)

# def dfs(i,arr):
#     global add, sub, mul, div, max_value, min_value
#     if i == N :
#         max_value = max(max_value,arr)
#         min_value = min(min_value,arr)

#     else:
#         if add > 0 :
#             add -= 1
#             dfs(i+1, arr + num[i])
#             add += 1 # 각 케이스에 대한 출발 지점 돌려 놓기
#         if sub > 0 :
#             sub -= 1
#             dfs(i+1, arr - num[i])
#             sub += 1
#         if mul > 0 :
#             mul -= 1 
#             dfs(i+1, arr * num[i])
#             mul += 1
#         if div > 0 :
#             div -= 1
#             dfs(i+1, int(arr / num[i]))
#             div += 1

# dfs(1,num[0])

print(max_value)
print(min_value)




