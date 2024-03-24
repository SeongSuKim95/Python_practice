n = int(input())

seq = []
answer = 0

def is_beautiful():
    cur_idx = 0

    while cur_idx < n :

        if cur_idx + seq[cur_idx] - 1  >= n :
            return False
        
        for seq_idx in range(cur_idx,cur_idx+seq[cur_idx]):
            if seq[cur_idx] != seq[seq_idx]:
                return False
            
        cur_idx += seq[cur_idx]
        
    return True

        
def select(idx):
    global answer

    if idx == n :
        if is_beautiful():
            answer += 1
        return
    for i in range(1,n+1):
        seq.append(i)
        select(idx+1)
        seq.pop()

select(0)

print(answer)