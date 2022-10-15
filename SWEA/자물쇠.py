
N, K = map(int,input().split())

NUM = ''.join(list(input()))

step = N//4
rotate_list = []
for _ in range(step):
    temp = NUM[1:]
    temp = temp+NUM[0]
    rotate_list.append(temp)
    NUM = temp

NUM_list = []

for NUM in rotate_list:
    for i in range(0,N,step):
        NUM_list.append(int(NUM[i:i+step],16))

print(sorted(set(NUM_list),reverse=True)[K-1])