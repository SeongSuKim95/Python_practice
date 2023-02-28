from collections import deque

N = int(input())

def calc(num,idx):

    if idx == 1:
        num -= 1
    elif idx == 2:
        num += 1
    elif idx == 3:
        num = num // 2
    elif idx == 4 :
        num = num // 3
    return num


def bfs():

    q = deque()
    q.append(N)
    qlen = len(q)
    cnt = 0
    while q :        
        if 1 in q:
            return cnt
        cnt += 1
        nq = []
        for _ in range(qlen):
            cur_num = q.popleft()
            nq.append(calc(cur_num,1))
            nq.append(calc(cur_num,2))
            if not cur_num % 2:
                nq.append(calc(cur_num,3))
            if not cur_num % 3:
                nq.append(calc(cur_num,4))
        
        nq = deque(list(set(nq)))        
        qlen = len(nq)
        q = nq.copy()

print(bfs())
