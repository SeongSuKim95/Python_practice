K, N = list(map(int,input().split()))
# 1이상 K이하의 숫자를 N번 선택
selectedList = []

def select(idx):
    if idx == N :
        print(*selectedList)
        return   
    for i in range(1,K+1):
        if idx == 0 or idx == 1 or not (selectedList[idx-1] == i and selectedList[idx-2] == i):
            selectedList.append(i)
            select(idx+1)
            selectedList.pop()

select(0)