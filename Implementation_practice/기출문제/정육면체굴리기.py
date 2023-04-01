FACE_NUM = 6

OUT_OF_GRID = (-1,-1)

n,m,x,y,k = list(map(int,input().split()))

grid = [
    list(map(int,input().split()))
    for _ in range(n)
]

turns = list(map(lambda x : int(x)-1, input().split()))

dirs = [(0,1),(0,-1),(-1,0),(1,0)]

dice = [0] * (FACE_NUM + 1)
# 동쪽 0 
# U , F , R  ---> 7 - R, F, U
# 서쪽 1
# U , F , R  ---> R, F, 7 - U
# 북쪽 2
# U , F , R  ---> F, 7 - U, R  
# 남쪽 3
# U , F , R  ---> 7 - F, U , R


def in_range(x,y):

    return 0<=x<n and 0<=y<m

def simulate():
   
    U, F, R = 1,2,3
    cx,cy = x,y
    for dir in turns :
        dx,dy = dirs[dir]
        nx,ny = cx + dx, cy + dy
        if in_range(nx,ny) : 
            if dir == 0 : # 동
                if grid[nx][ny] : # 칸에 숫자 있으면
                    dice[R] = grid[nx][ny]
                    grid[nx][ny] = 0
                else :
                    grid[nx][ny] = dice[R]
                U, F, R = 7 - R, F, U
            elif dir == 1: # 서
                if grid[nx][ny]:
                    dice[7-R] = grid[nx][ny]
                    grid[nx][ny] = 0
                else : 
                    grid[nx][ny] = dice[7-R]
                U, F, R = R, F, 7 - U
            elif dir == 2: # 북
                if grid[nx][ny]:
                    dice[7-F] = grid[nx][ny]
                    grid[nx][ny] = 0
                else :
                    grid[nx][ny] = dice[7-F]
                U, F, R = F, 7 - U, R
            elif dir == 3: # 남
                if grid[nx][ny]:
                    dice[F] = grid[nx][ny]
                    grid[nx][ny] = 0
                else :
                    grid[nx][ny] = dice[F]
                U, F, R = 7 - F, U ,R
            cx,cy = nx,ny
            print(dice[U])

simulate()