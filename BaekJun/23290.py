import copy

M, S = map(int,input().split())

fish = [list(map(int,input().split())) for _ in range(M)]

fdlist = [[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
sdlist = [[-1,0],[0,-1],[1,0],[0,1]]

_map = [[[] for _ in range(4)] for _ in range(4)]
_smell = [[0] *4 for _ in range(4)]

for fx,fy,fd in fish:
    _map[fx-1][fy-1].append(fd-1)


shark = tuple(map(lambda x: int(x)-1,input().split()))


def move_fish():
    res = [[[] for _ in range(4)] for _ in range(4)]

    for row in range(4):
        for col in range(4):
            while _temp[row][col]:
                f = _temp[row][col].pop()
                for i in range(f,f-8,-1):
                    i %= 8
                    nrow, ncol = row + fdlist[i][0], col + fdlist[i][1]
                    if 0<= nrow < 4 and 0<= ncol <4 and (nrow,ncol) != shark and _smell[nrow][ncol] == 0:
                        res[nrow][ncol].append(i)
                        break
                else:
                    res[row][col].append(f)
    return res

def dfs(x,y,depth,cnt,visit):

    global eat, shark, max_eat

    if depth == 3:
        if max_eat < cnt :
            max_eat = cnt
            shark = (x,y)
            eat = visit[:]
        return
    else:
        for dir in sdlist:
            nx,ny = x + dir[0], y + dir[1]
            if nx<0 or  nx>=4 or ny<0 or ny>=4:
                continue
            if (nx,ny) not in visit:
                visit.append((nx,ny))
                dfs(nx,ny,depth+1,cnt+len(_temp[nx][ny]),visit)
                visit.pop()
            else:
                dfs(nx,ny,depth+1,cnt,visit)



for _ in range(S):

    eat = []
    visited = []
    max_eat = -1

    _temp = copy.deepcopy(_map)

    _temp = move_fish()

    dfs(shark[0],shark[1],0,0,visited) # depth, cnt

    for x,y in eat:
        if _temp[x][y]:
            _temp[x][y] = []
            _smell[x][y] = 3
    for i in range(4):
        for j in range(4):
            if _smell[i][j]:
                _smell[i][j] -= 1
    
    for i in range(4):
        for j in range(4):
            _map[i][j] += _temp[i][j]
answer = 0

for i in range(4):
    for j in range(4):
        answer+=len(_map[i][j])

print(answer)