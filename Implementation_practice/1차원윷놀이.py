cn,m,k = list(map(int,input().split()))

dists = list(map(int,input().split()))

answer = []
max_score = 0
scores = [0] * (k + 1)

def get_score():
    score = 0
    for pos in scores :
        if pos >= m - 1 :
            score += 1
    return score


def select_num(cnt):
    global max_score
    
    score = get_score()
    max_score = max(max_score,score)
    
    if cnt == n :
        return
    for i in range(1,k+1):
        if scores[i] >= m-1 :
            continue
        scores[i] += dists[cnt]
        select_num(cnt + 1)
        scores[i] -= dists[cnt]

select_num(0)
print(max_score)