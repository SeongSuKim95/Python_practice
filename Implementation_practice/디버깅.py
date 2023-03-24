n, m, h = list(map(int,input().split()))

'''
1 <= a <= h, 1 <= b <= n-1
'''
lines = [tuple(map(int,input().split())) for _ in range(m)]

line_map = {i : [] for i in range(h+1)}

customer = [i for i in range(n+2)]

min_lines = 4

for a,b in lines :
    line_map[a].append(b)

def get_result():
    result = customer[:]
    for line in line_map.values() :
        
        for b in line:
            temp1,temp2 = result[b], result[b+1]
            result[b] = temp2
            result[b+1] = temp1

    return customer[1:] == result[1:]

def can_make(a,b):

    return not(b-1 in line_map[a] or b+1 in line_map[a] or b in line_map[a])


def dfs(cnt):
    global min_lines

    if cnt >= min_lines:
        return

    if cnt > 3: 
        return

    if get_result():
        min_lines = min(min_lines,cnt)
        return
    
    for a in line_map.keys():
        for b in range(1,n+1):
            if can_make(a,b):
                line_map[a].append(b)
                dfs(cnt + 1)
                line_map[a].pop()

dfs(0)

if min_lines == 4:
    print(-1)
else :
    print(min_lines)
