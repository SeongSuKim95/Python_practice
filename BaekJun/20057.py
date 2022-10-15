N = int(input())

_map = [list(map(int,input().split())) for _ in range(N)]

init_sand = sum([sum(row) for row in _map])


# 좌 --> [-1,1] [0,-1]
# 하 --> [-1,-1] [1,0]
# 우 --> [1,-1] [0,1]
# 상 --> [1,1]  [-1,0]


#   1 x 1
# 2 7 y 7 2
#  10 a 10 
#     5
# 좌 하 우 상
_dirlist = {0: [0,-1], 1: [1,0], 2: [0,1], 3: [-1,0]}

_sandlist = { 
              0: {(-1,1):0.01, (1,1): 0.01, (1,0) :0.07, (-1,0):0.07, (-2,0): 0.02, (2,0): 0.02, (1,-1): 0.1, (-1,-1): 0.1, (0,-2): 0.05}, 
              1: {(-1,-1):0.01, (-1,1):0.01, (0,1) : 0.07, (0,-1):0.07, (0,2): 0.02, (0,-2): 0.02, (1,-1):0.1, (1,1): 0.1, (2,0) : 0.05},
              2: {(1,-1):0.01, (-1,-1):0.01, (-1,0) : 0.07, (1,0):0.07, (2,0): 0.02, (-2,0): 0.02, (-1,1):0.1, (1,1): 0.1, (0,2) : 0.05},
              3: {(1,1):0.01, (1,-1):0.01, (0,-1) : 0.07, (0,1):0.07, (0,-2): 0.02, (0,2): 0.02, (-1,1):0.1, (-1,-1): 0.1, (-2,0) : 0.05}
            }

x, y = int(N//2), int(N//2)
_dir_round = 0
_dir_seq = [0,1,2,2,3,3]
_dir_idx = 0 

def check(x,y):

    if 0 <= x < N and 0<= y < N:
        return True
    else :
        return False

while (x,y) != (0,0):
    
    _dir = _dir_seq[_dir_idx]

    x,y = x + _dirlist[_dir][0], y + _dirlist[_dir][1]
    # print(f"dir:{_dir},x:{x},y:{y}")
    sum_sand = 0
    for coord, ratio in _sandlist[_dir].items():
        if check(x + coord[0],y + coord[1]) :
            _map[x + coord[0]][y + coord[1]] += int(_map[x][y] * ratio)
        sum_sand += int(_map[x][y]*ratio)
    if check(x+_dirlist[_dir][0],y+_dirlist[_dir][1]):
        _map[x+_dirlist[_dir][0]][y+_dirlist[_dir][1]] += _map[x][y] - sum_sand
    _map[x][y] = 0

    _dir_idx += 1 
    if _dir_idx == len(_dir_seq):
        _dir_idx = 0
        _dir_round += 1
        temp = 2*_dir_round + 1
        _dir_seq = [0] * temp + [1] * temp + [2] * (temp+1) + [3] *(temp+1) 
    # for row in _map:
    #         print(row)
    # print('\n')
final_sand = sum([sum(row) for row in _map])

print(init_sand - final_sand)
