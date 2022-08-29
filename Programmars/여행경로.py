# from collections import defaultdict, deque

# answer = []
# def dfs(start,data,route):
#     global answer
#     route.append(start)
    
#     for area in data[start]:
#         if data[area]:
#             dfs(area,data,route)
#         else:
#             print(route)


# def solution(tickets):
#     global answer
#     data = defaultdict(list)    
#     for a,b in tickets:
#         data[a].append(b)  
#     start = "ICN"
#     route = []
#     dfs(start,data,route)        
#     print(answer)
    
#     return answer

from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    
    # 각 시작점의 인접 리스트 구하기
    for key, value in tickets:
        graph[key].append(value)
        
    # 딕셔너리의 value(도착점) 알파벳순 정렬
    # 각 도착점에 대해 미리 정렬을 해놓으면 됨
    for g in graph:
        graph[g].sort()

    answer = dfs(graph) # dfs 수행 Graph만 들어가면 되잖아!
    
    return answer

# dfs 수행 메서드
def dfs(graph):
    answer = [] # 경로
    stacks = ['ICN'] # 스택
    
    while stacks:
        stack = stacks[-1] # 가장 위에 있는 데이터
        
        if stack not in graph or len(graph[stack]) == 0: # 시작점에 없거나 더 이상 갈 곳이 없는 경우
            answer.append(stacks.pop())
        else:
            stacks.append(graph[stack].pop(0))
            
    return answer[::-1] # 역순 출력