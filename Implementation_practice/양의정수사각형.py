# N, M = map(int,input().split())

# map_ = [list(map(int,input().split())) for _ in range(N)]

def check(i,j,k,l):
    for row in range(i,j+1):
        for col in range(k,l+1):
            if map_[row][col]<= 0 :
                return False
    return True

def main():
    max_size = 0
    for i in range(N):
        for j in range(i,N):
            for k in range(M):
                for l in range(k,M):
                    if check(i,j,k,l):
                        max_size = max(max_size,(j-i+1)*(l-k+1))
    if max_size :
        print(max_size)
    else :
        print(-1)
map_ = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

print(map_[1:3][2:3])