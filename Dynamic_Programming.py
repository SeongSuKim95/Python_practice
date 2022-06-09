# Dynamic Programming
# 이미 계산된 결과를 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 하는 것이 개념의 핵심
# Dynamic Allocation :  프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법

# 피보나치 수열 : 수열에 대한 기록? --> 배열 또는 리스트, table에 기록


def fibo(x):
    if x==1 or x==2 : # 함수 종료 명시 
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))

# 피보나치 수열은 지수 시간의 복잡도를 가진다. ex: f(2)를 구하기 위해 중복적인 호출을 하게된다.
# 다이나믹 프로그래밍을 통해 시간 복잡도를 줄이는 방법 : Cacheing!

d = [0] * 100

def fibo_dp(x):
    if x==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

# Bottom up method

# d[1] = 1
# d[2] = 1
# n = 99

# for i in range(3,n+1):
#     d[i] = d[i-1] + d[i-2]

# print(d[n])

# ai = i번쨰 식량창고까지의 최적의해(얻을 수 있는 식량의 최댓값)
# ki = i번째 식량창고에 있는 식량의 양
# a_i = max(a_(i-1),a_(i-2)+k_i)

#  i-1번째 최적의해 VS i-2번째 최적의 해 + i번째 식량창고
n = int(input())
array = list(map(int,input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0],array[1])

for i in range(2,n):

    d[i] = max(d[i-1],d[i-2]+array[i])

print(d[n-1])

# 최적 부분 구조 : i 번째 최적 값을 구하기 위해 i-1번째까지의 최적값이 사용

# f(6) --> f(5), f(3), f(2)중 min 값 사용
# ai = i를 1로 만들기 위한 최소 연산 횟수
# ai= min(a_(i-1),a_(i/2),a_(i/3),a_(i/5)) +1

x = int(input())

d = [0] * 30001

for i in range(2,x+1):
    d[i] = d[i-1] +1
    if i%2 == 0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3 == 0 :
        d[i] = min(d[i],d[i//3]+1)
    if i%5 == 0 :
        d[i] == min(d[i],d[i//5]+1)

print(d[x])

n,m = map(int, input().split())

# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))
# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001: # i-k원을 만드는 방법이 존재하는 경우
            d[j] = min(d[i],d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else :
    print(d[m])


# Longest Increasing Subsequence (가장 긴 증가하는 부분 수열)
# D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
# 모든 0 <= j < i에 대하여, D[i] = max(D[i],D[j]+1) if array[j] < array[i]
# 시간 복잡도 O(n^2)

n = int(input())

array = list(map(int,input().split()))
array.reverse()

dp = [1] * n

for i in range(1,n):
    for j in range(0,i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))

