'''
내 코드  
'''
N = int(input())

lines_ = []
for _ in range(N):
    lines_.append(tuple(map(int,input().split())))

line_cnt = {i:0 for i in range(1,1001)}
answer = []
max_cnt = 0

def add_line(idx):
    global max_cnt

    if idx > N + 1 :
        return 
    if answer:
        if 2 not in line_cnt.values() :
            max_cnt = max(max_cnt,len(answer))
        else :
            return
    
    for i in range(idx,N):
        x1,x2 = lines_[i]
        
        answer.append((x1,x2))

        for j in range(x1,x2+1):
            line_cnt[j] += 1
        
        add_line(i+1)

        answer.pop()
        for j in range(x1,x2+1):
            line_cnt[j] -= 1
add_line(0)
print(max_cnt)

