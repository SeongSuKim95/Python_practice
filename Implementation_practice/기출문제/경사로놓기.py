n,L = list(map(int,input().split()))

grid = [list(map(int,input().split())) for _ in range(n)]

# 2 이상 차이나면 못감
# 1 차이나는 지점을 확인 (내려가는지, 올라가는지 확인)
# 내려가는 경우
# 같은 높이가 나타나면 다리를 놓는다.
# 올라가는 경우
# 지나온 길 중에 다리가 놓여있으면 패스
# 다리 길이만큼 놓는다. --> 놓는 도중 같은 높이가 아니면 pass

def can_slope_before(pos,lst,visited): # pos 위치 이전으로 다리를 놓을 수 있는지?
    
    height = lst[pos]
    # print(pos,lst,visited)
    if (pos+1) - L < 0  :
        return False
    else :
        for i in range(pos,pos-L,-1):
            if lst[i] != height or visited[i] == True :
                # print(i)
                return False
    return True

def can_slope_after(pos,lst,visited): # pos 위치 이후로 다리를 놓을수 있는지?

    height = lst[pos]
    if (pos - 1) + L >= len(lst):
        return False

    else :
        for i in range(pos,pos+L):
            if lst[i] != height or visited[i] == True :
                return False
    return True

def check(lst):
    
    visited = [0] * n

    for i in range(len(lst)-1):

        # 다음 칸과의 차이
        # 2 이상 차이나면 못감 
        if abs(lst[i] - lst[i+1])> 1 :
            return False
        
        if lst[i] - lst[i+1] == 1 : # 내려가는 경사로
            
            if can_slope_after(i+1,lst,visited) :
                
                for j in range(i+1,i+1+L):
                    visited[j] += 1
            else : # 경사로 못 놓으면 못 지나감
                return False

        elif lst[i+1] - lst[i] == 1 : # 올라가는 경사로

            if can_slope_before(i,lst,visited) :
                for j in range(i,i-L,-1):
                    visited[j] += 1 
            else : # 경사로 못 놓으면 못 지나감 
                return False
    
    for i in visited:
        if i > 1:
            return False
    return True

def check_all():
    cnt = 0 
    for row in grid:
        if check(row):
            # print(row)
            cnt += 1

    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(grid[j][i])
        if check(temp):
            # print(temp)
            cnt += 1
    return cnt

# print(check([1,1,2,2,2,2]))      
print(check_all())