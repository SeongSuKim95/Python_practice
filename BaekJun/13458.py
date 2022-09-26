
N = input()

room_num = list(map(int,input().split()))

main, sub = map(int,input().split())
answer = 0
for i in room_num:
    answer += 1
    if i > main:
        temp = (i-main)%sub
        if temp == 0 :
            answer += (i - main)//sub
        else:
            answer += (i - main)//sub + 1
print(answer)