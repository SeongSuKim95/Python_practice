
idx = int(input())
n = 1

while n*(n+1)/2 < idx :
    n += 1

col_idx = idx - n*(n-1)/2

if n % 2 :
    print("{}/{}".format(int(n+1 - col_idx), int(col_idx)))
else :
    print("{}/{}".format(int(col_idx),int(n+1-col_idx)))
