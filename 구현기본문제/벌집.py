# 1 6 1 
# 7 12 2
# 19 18 3
# 37  24
# 61   30

N = int(input())
num = 1
layer = 1
while num < N :
    num += 6 * layer
    layer += 1
print(layer)