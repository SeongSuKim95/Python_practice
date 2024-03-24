N = int(input())

lines = [
    tuple(map(int,input().split()))
    for _ in range(N)
]
selectedLines = []
answer = 0
def isDuplicate(line1,line2):
    ax1,ax2 = line1
    bx1,bx2 = line2
    return (ax1 <= bx1 and bx1 <= ax2) or (bx2 <= ax2 and ax1 <= bx2) or \
           (bx1 <= ax1 and ax1 <= bx2) or (ax2 <= bx2 and bx1 <= ax2)
# idx 번째 선분을 뽑거나 안뽑는 함수
def select(idx):
    global answer
    if idx == N :
        for i in range(len(selectedLines)) :
            for j in range(i+1,len(selectedLines)):
                if isDuplicate(selectedLines[i],selectedLines[j]):
                    return
        answer = max(answer,len(selectedLines))
        return  

    select(idx+1)

    selectedLines.append(lines[idx])
    select(idx+1)
    selectedLines.pop()

select(0)
print(answer)

