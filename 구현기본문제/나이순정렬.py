N = int(input())

datas = []
for i in range(1,N+1):
    age, name = list(input().split())
    datas.append((int(age),i,name))
datas.sort()
for age, _, name in datas:
    print(age,name)