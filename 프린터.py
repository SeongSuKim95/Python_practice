# 내풀이

priorities = [2,1,3,3,2]
location = 2
cnt = 0
max_prior = max(priorities)
# while True:
#     for i in range(len(priorities)):
#         if priorities[i] == max_prior:
#             priorities[i] = 0
#             cnt += 1 
#             max_prior = max(priorities)
#             if i == location:
#                 print(cnt)
#                 break


# 정답

queue =  [(i,p) for i,p in enumerate(priorities)]

answer = 0
while True:
    cur = queue.pop(0)
    if any(cur[1] < q[1] for q in queue):
        queue.append(cur)
    else:
        answer += 1
        if cur[0] == location:
            print(answer)
            break