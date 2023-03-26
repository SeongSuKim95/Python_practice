# 몬스터 종류 1,2,3
# 좌 하 우 상
dirs_pattern = [(0,-1),(1,0),(0,1),(-1,0)]
# 우 하 좌 상
dirs_magic = [(0,1),(1,0),(0,-1),(-1,0)]

EMPTY = 0

n,m = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

attack = []
score = 0

for _ in range(m):
    attack.append(tuple(map(int,input().split())))

pattern,d = [],0
for i in range(1,n):
    pattern.append((i,d))
    d = (d+1+4)%4
    pattern.append((i,d))
    d = (d+1+4)%4
pattern.append((n-1,d))
sx,sy = n//2,n//2
coords = []
for r,d in pattern :
    for _ in range(r):
        sx,sy = sx + dirs_pattern[d][0], sy + dirs_pattern[d][1]
        coords.append((sx,sy))

def do_attack(d,p):
    global score

    sx,sy = n//2, n//2
    dx,dy = dirs_magic[d]

    for _ in range(p):
        sx, sy = sx + dx, sy + dy
        score += grid[sx][sy]
        grid[sx][sy] = EMPTY

def get_cur_state():
    lst = []
    for x,y in coords:
        lst.append(grid[x][y])
    return lst

def print_array(array):

    for row in array:
        print(*row)
    print("#########")

def explosion(cur_state):
    global score

    while True:
        last_elem = 0
        cnt = 0
        new_state = []
        # print(cur_state)
        for cur_elem in cur_state:
            if cur_elem :
                if last_elem == 0:
                    last_elem = cur_elem
                    cnt = 1
                else :
                    if cur_elem == last_elem:
                        cnt += 1
                    elif cur_elem != last_elem:
                        if cnt < 4 :
                            for _ in range(cnt): 
                                new_state.append(last_elem)
                            last_elem = cur_elem
                            cnt = 1
                        else :
                            score += cnt * last_elem
                            last_elem = cur_elem
                            cnt = 1
    
        if cnt < 4 :
            for _ in range(cnt):
                new_state.append(last_elem)
        else :
            score += cnt * last_elem

        if cur_state == new_state:
            break
        else:
            cur_state = new_state[:]
    return cur_state

def extend_state(state):
    
    new_state = []
    cnt,last_elem = 0,0
    for cur_elem in state:
        if last_elem == 0:
            last_elem = cur_elem
            cnt += 1
        else:
            if cur_elem != last_elem:
                new_state.append(cnt)
                new_state.append(last_elem)
                last_elem = cur_elem
                cnt = 1
            else :
                cnt += 1
    new_state.append(cnt)
    new_state.append(last_elem)

    return new_state[:len(coords)]

def fill(state):
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = EMPTY

    for i in range(len(state)):
        cur_x,cur_y = coords[i]
        grid[cur_x][cur_y] = state[i]

for d,p in attack:
    do_attack(d,p)
    cur_state = get_cur_state()
    new_state = explosion(cur_state)
    final_state = extend_state(new_state)
    fill(final_state)
print(score)
