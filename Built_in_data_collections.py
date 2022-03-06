# Collections : 유용한 자료구조 ex) deque, Counter
# list는 삭제, 삽입이 모두 '가장 뒤쪽 원소' 기준인 반면
# deque 사용시 popleft()로 첫번째 원소 삭제, append(x)로 마지막 인덱스에 삽입함
# pop()을 마지막 원소 삭제, appendleft(x) 로 첫번째 인덱스에 삽입가능
from collections import deque

data = deque([2,3,4])

data.appendleft(1)
data.append(5)

print(data) # deque[1,2,3,4,5]
print(list(data))# list 자료형으로 반환

from collections import Counter

counter = Counter(['r','b','r','b','g','b'])
print(counter['b']) # 'b'등장횟수, 3
print(dict(counter)) # { 'r':2,'b' : 3,'g':1}