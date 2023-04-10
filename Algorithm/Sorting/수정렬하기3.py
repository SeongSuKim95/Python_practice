import sys
# 메모리 사용을 줄이기 위해 배열을 선언 후에 입력된 숫자만큼 cnt
# 배열의 idx는 이미 정렬되어 있는 수열과 같다.

N = int(input())
cnt_list = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    cnt_list[num] += 1


for i in range(1,10001):
    if cnt_list[i] :
        for j in range(cnt_list[i]):
            print(i)