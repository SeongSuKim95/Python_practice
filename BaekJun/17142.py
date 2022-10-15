from collections import deque

N,M = map(int,input().split())

_map = [list(map(int,input().split())) for _ in range(N)]

def comb(arr,n):

	result = []

	if n <= 0  :
		return result
	elif n == 1 :
		for i in arr:
			result.append([i])
	else:
		
		for i in range(len(arr)-n+1):
			for j in comb(arr[i+1:],n-1):
				result.append([arr[i]]+j)
			
	return result

_virus_list = []
blank_cnt = 0
for row in range(N):
	for col in range(N):
		if _map[row][col] == 2:
			_virus_list.append((row,col))
		elif _map[row][col] == 0:
			blank_cnt +=1

_virus_combi = comb(_virus_list,M)
# print(_virus_combi)
_dirlist = [[-1,0],[0,1],[0,-1],[1,0]]
answer = 1e9

def bfs(q,blank):

	time = 0
	visited = [[0] * N for _ in range(N)]
	while True :
		len_q = len(q)

		if blank == 0 or len_q == 0:
			if blank == 0:
				return time
			else :
				return 1e9
		time += 1
		for i in range(len_q):
			row,col = q.popleft()
			if not visited[row][col]:
				visited[row][col] = 1	
			for dir in _dirlist:
				nrow = row + dir[0]
				ncol = col + dir[1]

				if 0<=nrow < N and 0<= ncol < N:
					if visited[nrow][ncol] == 0 :
						if _map[nrow][ncol] == 0 :
							visited[nrow][ncol] = 1
							q.append((nrow,ncol))
							blank -=1
						elif _map[nrow][ncol] == 2:
							visited[nrow][ncol] = 1
							q.append((nrow,ncol))						


for virus_set in _virus_combi:
	q= deque()
	for virus in virus_set:
		q.append(virus)
	tmp = bfs(q,blank_cnt)
	answer = min(answer,tmp)

if answer == 1e9:
	print(-1)
else:
	print(answer)



