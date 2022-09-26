
N = int(input())
apple = []
# print(dummy)
K = int(input())
for i in range(K):
    y,x = map(int,(input().split()))
    apple.append([y,x])

dir_num = int(input())
chdir = {}
for _ in range(dir_num):
    t, d = input().split()
    chdir[int(t)] = d 
head_y,head_x = 1,1
head_history = [[head_y,head_x]]
# index 0을 머리로, -1을 꼬리로
time,snake_dir,snake_len = 0,0,1

# 동 남 서 북
direction = {0:[0,1],1:[1,0],2:[0,-1],3:[-1,0]}

while True:  
    # 방향 바꾸는 코드
    if time in chdir.keys():
        if chdir[time] == "L": # 좌로 90도
            snake_dir -= 1
            if snake_dir < 0 :
                snake_dir = 3
        else: # "D", 우로 90도
            snake_dir += 1
            if snake_dir > 3:
                snake_dir = 0
                
    head_y += direction[snake_dir][0]
    head_x += direction[snake_dir][1]
    
    head_history.append([head_y,head_x])
    time += 1
    # 종료 조건
    if head_y < 1 or head_x < 1 or head_y > N or head_x > N : # 맵 밖으로 나간 경우
        break

    if [head_y,head_x] in apple: 
        apple.remove([head_y,head_x])
        snake_len += 1 

    if head_history[-(snake_len+1):].count([head_y,head_x]) != 1 :
        break

print(time)


# 0 A A 0 A A A 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0



