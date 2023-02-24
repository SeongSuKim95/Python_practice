'''
내코드
'''
N,M = list(map(int,input().split()))
lines = []
for _ in range(M):
    row,col = list(map(int,input().split()))
    lines.append([[row,col],[row+1,col]])
    lines.append([[row+1,col],[row,col]])

starts = [[i,1] for i in range(1,N+1)]
max_col = sorted(lines,key= lambda x : x[1][1])[-1][1][1]
min_cnt = 1e9
selected_lines = []

def ladders(lines):
    answer = []
    for idx,point in enumerate(starts):

        cur_point = point[:]
        while cur_point[1] != max_col+1 :
            for line in lines :
                if cur_point ==  line[0] :
                    cur_point = line[1][:]
                    break
            cur_point[1] += 1
        answer.append(cur_point[0])

    return answer

line_pair = []
target_answer = ladders(lines)

def select_lines(idx):
    global min_cnt
    if ladders(line_pair) == target_answer:

        min_cnt = min(min_cnt, len(line_pair)//2)
        return

    if idx > 2 * M:
        return

    for i in range(idx,2*M,2):

        line_pair.append(lines[i])
        line_pair.append(lines[i+1])

        select_lines(idx+2)

        line_pair.pop()
        line_pair.pop()

select_lines(0)
print(min_cnt)