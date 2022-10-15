N,M = map(int,input().split())

_map = [list(map(int,input().split())) for _ in range(N)]

coord_list = []
_dirlist = [[-1,0],[1,0],[0,-1],[0,1]]

def comb(arr,n):
    result =  []
    if n > len(arr):
        return result
    if n == 1 :
        for i in arr:
            result.append([i])
    elif n > 1:

        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:],n-1):
                result.append([arr[i]]+j)
    return result



def dfs(row,col,map):

    map[row][col] = 3
    for dir in _dirlist:
        nrow = row + dir[0]
        ncol = col + dir[1]
        if nrow <0 or nrow >= N or ncol <0 or ncol >=M or map[nrow][ncol] != 0:
            continue
        else:
            if map[nrow][ncol] == 0 :
                dfs(nrow,ncol,map)

answer = -1e9

for row in range(N):
    for col in range(M):
        if _map[row][col] == 0 :
            coord_list.append([row,col])
        
for coords in comb(coord_list,3):
    # map 깊은 복사
    for _ in range(N):
        _nmap = [row[:] for row in _map]

    for coord in coords:
        _nmap[coord[0]][coord[1]] = 1

    for row in range(N):
        for col in range(M):
           if _nmap[row][col] == 2:
                dfs(row,col,_nmap)    
    cnt = 0
    for row in range(N):
        for col in range(M):
            if _nmap[row][col] == 0:
                cnt +=1

    answer = max(answer,cnt)

print(answer)