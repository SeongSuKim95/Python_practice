# 백준 9663

- 크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제
- N이 주어졌을때, 퀸을 놓는 방법의 수를 구하기!

<p align="center"><img src="https://user-images.githubusercontent.com/62092317/197951254-ded9d6b1-1dc3-40a2-a7da-24f220c2f637.png"></p>

# IDEA

<p align="center"><img src="https://user-images.githubusercontent.com/62092317/197954594-0ac382f1-c22e-4b52-b39e-31b580a5c22f.png"></p>

- DFS를 이용하여 map의 위에서부터 한 줄(row)씩 순서대로 **Queen을 놓을 수 있는 위치**를 탐색한다.
- 특정 row에서 queen을 놓을 자리가 없다면?
    - 탐색을 중지한다(Back-tracking)

- 특정 row에서  queen을 놓을 수 있는지를 판단하는 방법
    - 놓을 위치를 기준으로 같은 행, 같은 열, 대각선 상의 모든 위치에 queen이 놓여 있지 않아야 한다. 

- 종료조건?
    - 마지막 줄까지 Queen을 놓을 자리가 존재할 경우! == N개의 퀸을 놓는 경우
    - 탐색을 중지하는 경우

# 구현

- 2차원 map이기 때문에 2차원 배열을 써야할 것 같지만 1차원 배열만으로도 위 IDEA를 구현할 수 있다!!
- List의 (Index,value)를 (row,col)으로 생각하는 것이 point!

<p align="center"><img src="https://user-images.githubusercontent.com/62092317/197955661-1158453f-33cd-4c02-a614-4d7178602eb3.png"></p>

- 좌우 검사 : 단순히 현재 queen의 column 위치와 기존에 적재된 queen 중 특정 queen의 column 위치가 같은지 확인하면 된다. (**board[n] == board[i]** 부분) 
- 대각선 검사 : (현재 queen의 raw - 기존의 queen의 raw)가 |현재 queen의 column - 기존 queen의 column| 과 같은지 확인하면 된다. (**n-i == abs(board[n] - board[i])**) 
