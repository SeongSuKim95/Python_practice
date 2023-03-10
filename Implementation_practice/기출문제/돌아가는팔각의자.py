
chairs = [input() for _ in range(4)]

k = int(input())

turn = [
    tuple(map(int,input().split()))
    for _ in range(k)
]

# 우측 접점 index : 2, 좌측 접점 index : 6
RIGHT, LEFT = 2,6
chairs_next = [''] * 4

def shift_table(table,dir):
    if dir == 1 : # clock
        temp = table[-1]
        result = temp + table[:-1]
    else : #counter clock
        temp = table[0]
        result = table[1:] + temp
    return result

def check_left(cur_idx,dir):
    # chairs_next[cur_idx] = shift_table(chairs[cur_idx],dir)
    Flag = True
    while cur_idx > 0 :
        if chairs[cur_idx][LEFT] != chairs[cur_idx-1][RIGHT] and Flag:
            chairs_next[cur_idx-1] = shift_table(chairs[cur_idx-1],-dir)
            cur_idx -= 1
            dir = -dir
        else :
            chairs_next[cur_idx-1] = chairs[cur_idx-1][:]
            cur_idx -= 1
            Flag = False

def check_right(cur_idx,dir):
    # chairs_next[cur_idx] = shift_table(chairs[cur_idx],dir)
    Flag = True
    while cur_idx < 3 :
        if chairs[cur_idx][RIGHT] != chairs[cur_idx+1][LEFT] and Flag:
            chairs_next[cur_idx+1] = shift_table(chairs[cur_idx+1],-dir)
            cur_idx += 1
            dir = -dir
        else :
            chairs_next[cur_idx+1] = chairs[cur_idx+1][:]
            cur_idx += 1
            Flag = False

def calc():
    
    return sum([int(chairs[i][0]) * (2 ** i) for i in range(4)])


for table_idx,dir in turn:
    cur_idx,cur_dir = table_idx-1,dir
    chairs_next[cur_idx] = shift_table(chairs[cur_idx],dir)
    check_left(cur_idx,cur_dir)
    check_right(cur_idx,cur_dir)
    chairs = chairs_next[:]
    chairs_next = [''] * 4


print(calc())