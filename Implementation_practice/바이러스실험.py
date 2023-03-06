def print_array():

    for row in virus_grid:
        print(*row)
    print("##")

n,m,k = list(map(int,input().split()))

food_grid = [[5 for _ in range(n)] for _ in range(n)]
food_supply = [list(map(int,input().split())) for _ in range(n)]

virus_grid = [[[] for _ in range(n)] for _ in range(n)]
virus_dead = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r,c,life = list(map(int, input().split()))
    virus_grid[r-1][c-1].append(life)
# print_array()


def in_range(x,y):

    return 0<=x<n and 0<=y<n


def step1():

    for i in range(n):
        for j in range(n):
            if virus_grid[i][j]:
                virus_temp= sorted(virus_grid[i][j][:])
                next_virus = []
                for idx,virus in enumerate(virus_temp):
                    food = food_grid[i][j]
                    if virus <= food :
                        food_grid[i][j] = food - virus
                        next_virus.append(virus + 1)
                    else :
                        virus_dead[i][j].append(virus)
                virus_grid[i][j] = next_virus
    # print_array()
def step2():

    for i in range(n):
        for j in range(n):
            if virus_dead[i][j]:
                for virus in virus_dead[i][j]:
                    food_grid[i][j] += virus // 2


def step3():

    dxs,dys = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]

    for i in range(n):
        for j in range(n):
            if virus_grid[i][j] :
                for virus in virus_grid[i][j]:
                    if not virus % 5:
                        for dx,dy in zip(dxs,dys):
                            nx,ny = i + dx, j + dy
                            if in_range(nx,ny):
                                virus_grid[nx][ny].append(1)

def step4():

    for i in range(n):
        for j in range(n):
            food_grid[i][j] += food_supply[i][j]

def initialize():

    for i in range(n):
        for j in range(n):
            virus_dead[i][j] = []

def count():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if virus_grid[i][j]:
                cnt += len(virus_grid[i][j])
    
    return cnt

for i in range(k):
    initialize()
    step1()
    step2()
    step3()
    step4()
    # print(i)
    # print_array()
print(count())