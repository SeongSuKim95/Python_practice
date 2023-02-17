N,M,Q = map(int,input().split())

def move(lst,dir):
    # 오른쪽 방향
    if dir == 1:
        temp = lst[-1]
        for i in range(M-1,0,-1):
            lst[i] = lst[i-1]
        lst[0] = temp

    # 왼쪽 방향
    if dir == -1:
        temp = lst[0]
        for i in range(M-1):
            lst[i] = lst[i+1]
        lst[-1] = temp

    return lst

def check(lst1,lst2):

    for i in range(M):
        if lst1[i] == lst2[i]:
            return True
    return False


def prop(map_,C,dir):

    if dir == "R" : dir_orig = -1
    else : dir_orig = 1
    C = C - 1
    orig_C = C
    # 해당 줄 바람
    map_[C] = move(map_[C],dir_orig)
    # 위쪽 방향
    dir_temp = dir_orig
    while C > 0 :
        temp = map_[C]
        if check(temp,map_[C-1]):
            dir_temp = -dir_temp
            map_[C-1] = move(map_[C-1],dir_temp)
            C -= 1
        else :
            break 
    dir_temp = dir_orig
    C = orig_C
    while C < N-1 :
        temp = map_[C]
        if check(temp,map_[C+1]):
            dir_temp = -dir_temp
            map_[C+1] = move(map_[C+1],dir_temp)
            C += 1
        else :
            break
    return map_

def print_map(map_):
    
    for row in map_:
        for elem in row:
            print(elem,end = " ")

        print()
def main():

    map_ = [list(map(int,input().split())) for _ in range(N)]

    winds_ = [list(map(str,input().split())) for _ in range(Q)]

    for wind in winds_:
        C, dir = int(wind[0]), wind[1]
        map_ = prop(map_,C,dir)
    
    print_map(map_)



main()