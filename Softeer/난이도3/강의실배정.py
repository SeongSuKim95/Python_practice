import sys
import heapq
import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    s, f = map(int,sys.stdin.readline().split())

    # f 기준으로 (f, s)가 heap 리스트 안에 들어간다.
    heapq.heappush(heap, (f, s))

# 초기값
v = 0
# 강의 수
count = 0
# heap 리스트가 0이 될때까지 반복한다.
while heap:
    # 가장 작은 원소를 삭제후 f, s에 넣는다.
    f, s = heapq.heappop(heap)

    # 시작시간이 초기값(종료시간)보다 크거나 같으면 카운터해준다.
    # 다음 기준값은 종료시간으로 초기화해준다.
    if s >= v:
        count += 1
        v = f

print(count)
