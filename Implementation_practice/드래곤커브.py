# 규칙
'''
Dx =   Ty - Ey + Ex
Dy =  -Tx + Ex + Ey
'''

n = int(input())

curves = [list(map(int,input().split())) for _ in range(n)]

mapper = {
    0: (0,1),
    1: (-1,0),
    2: (0,-1),
    3: (1,0)
}

grid = [[0] * 101 for _ in range(101)]

# 하나씩 커브 만들기
def make_curve(lst) :
    x,y,d,g = lst
    dir = mapper[d]
    # 1차 직선
    current = [(x,y),(x+dir[0],y+dir[1])]
    for _ in range(g):
        next_curve = current[:]
        Ex,Ey = current[-1]
        for Tx,Ty in current[:-1][::-1] :
            Dx,Dy = Ty - Ey + Ex, -Tx + Ex + Ey
            next_curve.append((Dx,Dy))
        current = next_curve[:]
    return current

def draw():

    for curve in curves :

        points = make_curve(curve)

        for x,y in points :

            grid[x][y] = 1

def is_rectangle(x,y):

    return grid[x][y] * grid[x+1][y] * grid[x][y+1] * grid[x+1][y+1]

def check():
    cnt = 0
    for x in range(100):
        for y in range(100):
            cnt += is_rectangle(x,y)
    return(cnt)



draw()
print(check())


    
