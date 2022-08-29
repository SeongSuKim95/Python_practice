# Combination을 이용한 풀이
from itertools import permutations

def solution(k, dungeons):
    answer = []
    # k : 유저의 현재 피로토
    # dungeons : ['최소 필요 피로도','소모 피로도']
    
    comb = permutations(dungeons,len(dungeons))
    for i in list(comb):
        temp = k 
        cnt = 0
        for dungeon in i:
            if temp >= dungeon[0]:
                temp -= dungeon[1]
                cnt +=1
            else:
                break
        answer.append(cnt)
  
    return max(answer)

## Back tracking을 이용한 풀이
answer = 0
N = 0
visited = []

k = 80
dungeons = [[80,20],[50,40],[30,10]]

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    print(f"cnt:{cnt},answer:{answer}")
    for j in range(N):
        print(f"k:{k},visited:{visited},j:{j}")
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            print(f"DD, j:{j}")
            visited[j] = 0
       


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

solution(k,dungeons)