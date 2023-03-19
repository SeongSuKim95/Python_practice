START,END = 0,-1
ROUTE_MAIN = [i*2 for i in range(21)] # route 0
ROUTE_10 = [0,10,13,16,19,25,30,35,40] # route 1
ROUTE_20 = [0,20,22,24,25,30,35,40] # route 2
ROUTE_30 = [0,30,28,27,26,25,30,35,40] # route 3

ROUTES = [
    ROUTE_MAIN,
    ROUTE_10,
    ROUTE_20,
    ROUTE_30
]


# 말이 도착칸에 도착하면 남은 이동횟수 상관없이 끝내기
# 10개의 턴, 도착하지 않은 말을 이동가능
# 시작,도착을 제외하고 말 겹칠 수 없음. (다른 말이 있는 곳으로는 이동 불가)
# 말이 한번의 이동을 마칠때마다 칸에 있는 점수가 추가됨

TURNS = list(map(int,input().split()))
HORSE = [[0,0],[0,0],[0,0],[0,0]] # pos, route 
score = []
max_score = 0

def is_horse(pos,route):
    
    for horse in HORSE:
        if horse == [pos,route]:
            return True
    # special check
    pos25 = [[5,1],[4,2],[5,3]]
    pos30 = [[6,1],[5,2],[6,3]]
    pos35 = [[7,1],[6,2],[7,3]]
    pos40 = [[20,0],[8,1],[7,2],[8,3]]

    pos_combi = None
    for special_pos in [pos25,pos30,pos35,pos40]:
        if [pos,route] in special_pos:
            pos_combi = special_pos
            break
    if pos_combi :
        for horse in HORSE:
            if horse in pos_combi:
                return True
    return False

def play(turn_idx,horse_idx):

    global max_score

    if turn_idx == 10 : # 10번 턴 다 사용시, 또는 모든 말이 도착 칸으로 갈 시..? 
        max_score = max(max_score,sum(score))
        return

    move_distance = TURNS[turn_idx]
    cur_pos, route_idx = HORSE[horse_idx]

    if cur_pos == END : # 이미 도착한 말이면 이동 X
        return

    cur_route, new_route = route_idx, route_idx
    new_pos = cur_pos + move_distance # 새로 옮길 위치
    
    # 모든 route의 도착 조건 
    if new_pos >= len(ROUTES[cur_route]):
        new_pos, new_route = END, END

    if new_pos != END:
        # MAIN route 에서 다른 route로 가기
        if cur_route == 0 : # main route에 있는 경우
            if ROUTES[cur_route][new_pos] == 10 :
                new_pos, new_route = 1,1
            elif ROUTES[cur_route][new_pos] == 20 :
                new_pos, new_route = 1,2
            elif ROUTES[cur_route][new_pos] == 30 :
                new_pos, new_route = 1,3
    
    if new_pos != END and is_horse(new_pos,new_route):
        return

    for idx in range(4):
        HORSE[horse_idx] = [new_pos,new_route]
        if new_pos != END:
            score.append(ROUTES[new_route][new_pos])
        play(turn_idx+1,idx)
        HORSE[horse_idx] = [cur_pos,route_idx]
        if new_pos != END:
            score.pop()


for idx in range(4): # 0번부터 4번 말 선택
    cur_horse = [row[:] for row in HORSE]
    play(0,idx)
    HORSE = [row[:] for row in cur_horse]
    score = []
print(max_score)