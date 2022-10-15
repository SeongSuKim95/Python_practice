# import sys; input = sys.stdin.readline

from collections import deque


def rotate_right(x, d):
    if x > 4 or gears[x - 1][2] == gears[x][6]:
        return

    if gears[x - 1][2] != gears[x][6]:
        rotate_right(x + 1, -d)
        gears[x].rotate(d)


def rotate_left(x, d):
    if x < 1 or gears[x][2] == gears[x + 1][6]:
        return

    if gears[x][2] != gears[x + 1][6]:
        rotate_left(x - 1, -d)
        gears[x].rotate(d)


gears = {}
for i in range(1, 5):
    gears[i] = deque((map(int, input())))

for _ in range(int(input())):
    x, d = map(int, input().split())

    rotate_right(x + 1, -d)
    rotate_left(x - 1, -d)
    gears[x].rotate(d)


ans = 0
for i in range(4):
    ans += gears[i + 1][0] * (2 ** i)

print(ans)

# def turn_LR(data,dir):
#     if dir == 1 :
#         last = data[-1]
#         data = last + data[:-1]
#     else : 
#         first = data[0]
#         data = data[1:] + first
#     return data

# wheels = [[]]
# for _ in range(4):
#     wheels.append(str(input())[:-1])
# N = int(input())
# data = [list(map(int,input().split())) for _ in range(N)]

# left_side = 6
# right_side = 2

# for datas in data:

#     # wheels[datas[0]] = turn_LR(wheels[datas[0]] ,datas[1]) 
#     # print(wheels)
#     dir = datas[1]
#     cur_data = datas[0]
#     while cur_data > 1: #왼쪽
#         dir = -dir
#         if wheels[cur_data][left_side] != wheels[cur_data-1][right_side]:
#             wheels[cur_data-1] = turn_LR(wheels[cur_data-1],dir)
#             cur_data -=1
#         else:
#             break
#     dir = datas[1]
#     cur_data = datas[0]
#     while cur_data < 4: # 오른쪽
#         dir = -dir
#         if wheels[cur_data][right_side] != wheels[cur_data+1][left_side]:
#             wheels[cur_data+1] = turn_LR(wheels[cur_data+1],dir)
#             cur_data +=1
#         else :
#             break
#     wheels[datas[0]] = turn_LR(wheels[datas[0]],datas[1])     
    
# wheels.pop(0)
# temp = [i[0] for i in wheels]
# score = 0
# for idx, pole in enumerate(temp) :
#     score += int(pole) * 2**(idx)
# print(score)