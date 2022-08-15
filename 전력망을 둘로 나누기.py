from collections import defaultdict, deque


def bfs_and_node_count(del_line, n, wire_dict):  # bfs 수행과 연결된 노드수 구하기
    count = 1  # 연결된 노드 수
    print(f"del_line:{del_line}")
    visited = [False] * (n + 1)  # 방문여부 체크
    visited[del_line[0]] = True  # 시작 노드 방문 처리
    queue = deque([del_line[0]])

    while queue:  # bfs 수행
        print(f"queue:{queue}")
        curr = queue.popleft()
        print(f"curr:{curr}")
        for idx,i in enumerate(wire_dict[curr]):  # curr 노드와 연결된 노드에 대해서
            print(f"{idx}-th connected node: {i}")
            if visited[i] or i == del_line[1]:  # 방문했거나 끊어지는 부분의 노드인 경우 패스 ! 끊는 경우에 노드수를 구하늑 거니까..
                continue
            count += 1
            queue.append(i) # 연결된 node append
            visited[i] = True
            print(f"cnt:{count},visited:{visited}")
    print("#####################")
    return count


def solution(n, wires):
    answer = 1000
    data = defaultdict(set)  # 각 노드별 연결된 노드 정보
    for a, b in wires:
        data[a].add(b)
        data[b].add(a)
    print(data)
    print(wires)
    for w in wires:
        # 해당 와이어를 끊었을 때 한쪽 영역의 노드 수 구하기
        temp = bfs_and_node_count(w, n, data)
        # 기존 answer와 현재 해당하는 와이어를 끊었을 때 노드 차이 비교해서 최솟값으로 업데이트
        answer = min(answer, abs(n - temp - temp))
    return answer


n = 9 
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n,wires))

# BFS 로 한쪽의 노드수만 구하면 되는 문제이다. 왜냐하면 tree 형태로 주어지기 떄문에, 한쪽을 끊으면 두개의 tree가 생성된다는 것이 보장된다.