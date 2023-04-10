N = int(input())

def prime_list(n):

    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] :
            for j in range(2*i,n,i):
                sieve[j] = False
    
    return [i for i in range(2,n) if sieve[i]]

lst = [0] + prime_list(N+1)

k = len(lst)

prefix_sum = [0 for _ in range(k)]

for i in range(1,k):
    prefix_sum[i] = prefix_sum[i-1] + lst[i]
p1,p2,cnt = 0,0,0
# print(lst,prefix_sum)
while p1 < k and p2 < k :
    if prefix_sum[p1] - prefix_sum[p2] < N : 
        p1 += 1
    elif prefix_sum[p1] - prefix_sum[p2] == N :
        cnt += 1
        p1 += 1
    elif prefix_sum[p1] - prefix_sum[p2] > N :
        p2 += 1
print(cnt)

        


