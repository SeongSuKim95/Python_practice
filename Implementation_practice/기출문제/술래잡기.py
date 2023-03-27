n,m,h,k = list(map(int,input().split()))

# 상 우 하 좌
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

runners = [tuple(map(lambda x : int(x)-1,input().split())) for _ in range(m)]

run_grid = [
    [[] for _ in range(n)]
    for _ in range(n)
]

def print_array(array):
    for row in array:
        print(*row)
    print()

# 좌우 이동 도망자 0 --> 오른쪽 시작
# 상하 이동 도망자 1 --> 아래쪽 시작
run_dir_mapper = { 
    0 : 1,
    1 : 2
}

for x,y,d in runners :
    run_grid[x][y].append(run_dir_mapper[d])

trees = [tuple(map(lambda x : int(x)-1, input().split())) for _ in range(h)]

tree_grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for x,y in trees :
    tree_grid[x][y] = 1

def make_plen():
    p_lens = []
        
    for i in range(1,n):
        p_lens.append(i)
        p_lens.append(i)
    p_lens.append(i)
    p_lens.append(i)

    for i in range(n-1,0,-1):
        p_lens.append(i)
        p_lens.append(i)

    return p_lens

def make_pdirs():

    p_dirs = []
    sdir = 0
    for _ in range(2*(n-1)):
        p_dirs.append(sdir)
        sdir = (sdir + 1 + 4) % 4    
    p_dirs.append(sdir)

    sdir = 2
    for _ in range(2*(n-1)):
        p_dirs.append(sdir)
        sdir = (sdir - 1 + 4) % 4
    p_dirs.append(sdir)

    return p_dirs

def make_patterns():
    sx,sy,sd = n//2, n//2, 0 
    p_len = make_plen()
    p_dirs = make_pdirs()

    patterns = [(sx,sy,sd)]
    next_dirs = p_dirs[1:] + [p_dirs[0]]

    for cur_len,cur_dir,next_dir in zip(p_len,p_dirs,next_dirs):
        
        for _ in range(cur_len-1):
            dx,dy = dirs[cur_dir]
            sx,sy = sx+dx,sy+dy
            patterns.append((sx,sy,cur_dir))
        
        dx,dy = dirs[cur_dir]
        sx,sy = sx+dx,sy+dy
        patterns.append((sx,sy,next_dir))
    # print(patterns[1:])

    iters = k // len(patterns[1:])

    patterns = patterns[1:] * (iters + 1)
    
    return patterns
# 상 우 하 좌 
# 0 1 2 3
# print(make_patterns())
def in_range(x,y):

    return 0<=x<n and 0<=y<n

def can_go(x,y):

    return (x,y) != (sx,sy)

def is_close(x,y):

    return abs(x-sx) + abs(y-sy) <=3

def run():

    new_run_grid = [
        [[] for _ in range(n)]
        for _ in range(n)
    ]
    # print("run")
    # print(sx,sy)
    for i in range(n):
        for j in range(n):
            if run_grid[i][j]:
                if is_close(i,j):
                    for runner_dir in run_grid[i][j]:
                        # print(i,j)
                        cx , cy = i,j
                        nx , ny = cx + dirs[runner_dir][0], cy + dirs[runner_dir][1]
                        if in_range(nx,ny):
                            if not can_go(nx,ny):
                                new_run_grid[cx][cy].append(runner_dir)
                            else :
                                new_run_grid[nx][ny].append(runner_dir)
                        else :
                            runner_dir = (runner_dir + 2 + 4) % 4
                            nx, ny = cx + dirs[runner_dir][0], cy + dirs[runner_dir][1]
                            if not can_go(nx,ny):
                                new_run_grid[cx][cy].append(runner_dir)
                            else :
                                new_run_grid[nx][ny].append(runner_dir)
                else :
                    for runner_dir in run_grid[i][j]:
                        new_run_grid[i][j].append(runner_dir) 
                
    for i in range(n):
        for j in range(n):
            run_grid[i][j] = new_run_grid[i][j][:]

def catch(sx,sy,sdir,turn):
    global score
    for d in range(3):
        cx , cy = sx + d * dirs[sdir][0] , sy + d * dirs[sdir][1]
        if in_range(cx,cy) and not tree_grid[cx][cy] and run_grid[cx][cy]:
            score += turn * len(run_grid[cx][cy])
            run_grid[cx][cy] = []

# print_array(run_grid)
patterns = make_patterns()
# print(patterns)
sx,sy,sd = n//2, n//2, 0 
score = 0
for i in range(k):
    run()
    pre_score = score
    sx,sy,sdir = patterns[i]
    catch(sx,sy,sdir,i+1)

print(score)