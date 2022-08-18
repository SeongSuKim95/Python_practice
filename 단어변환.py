
#내코드
from collections import deque

answer = []
def dfs(start,data,target_idx,visited,cnt):
    global answer
    visited[start] = True
    cnt +=1
    for nodes in data[start]:
        if visited[nodes] == False and nodes != target_idx:
            dfs(nodes,data,target_idx,visited,cnt)
        elif nodes == target_idx:
            answer.append(cnt)

def bfs(start,data,target_idx,visited,cnt):
    
    global answer
    visited[start] = True
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        cnt +=1
        for nodes in data[curr]:
            if visited[nodes] == False and nodes != target_idx:
                queue.append(nodes)
                visited[nodes] = True
            elif nodes == target_idx:
                answer.append(cnt-1)

def solution(begin, target, words):
    global answer
    # 단어별로 글자가 한개씩만 다른 관계를 표현
    words = [begin] + words
    data = [[] for _ in words]
    
    for idx_i,i in enumerate(words):
        for idx_j,j in enumerate(words):
            if len(set(i)|set(j)) == 4:
                data[idx_i].append(idx_j)
                
    if target in words:
        target_idx = words.index(target)
    else:
        return 0
    
    visited = [False] * len(words)
    cnt = 0
    # bfs(0,data,target_idx,visited,cnt)
    dfs(0,data,target_idx,visited,cnt)
    return min(answer)



from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [ 0 for i in range(len(words))]
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break        
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i], cnt+1])
                    V[i] = 1
                    
    return answer


# 내코드 
# 
from collections import deque
answer = []
def dfs(begin,data,target,depth,words,visited):
    global answer

    visited[begin] = True
    for i in data[begin]:
        if visited[i] == False and words[i] != target:
            dfs(i,data,target,depth+1,words,visited)
        elif visited[i] == False and words[i] == target:
            answer.append(depth)
    
def solution(begin, target, words):
    
    words = [begin] + words
    data = [[] for _ in words]
    
    for idx_1,i in enumerate(words):
        for idx_2,j in enumerate(words):
            temp = 0
            for k in range(len(i)):
                if i[k] != j[k] :
                    temp +=1
            if temp == 1:
                data[idx_1].append(idx_2)
                
    visited = [False] * len(words)
    if target in words:    
        dfs(0,data,target,1,words,visited)
        if answer :
            return min(answer)
        else:
            return 0
    else:
        return 0
    
