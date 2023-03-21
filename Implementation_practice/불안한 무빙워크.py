n, k = list(map(int,input().split()))

safety = list(map(int,input().split()))

person = [False for _ in range(2 * n)]


def shift_right():
    global safety,person

    temp = safety[-1]
    safety = [temp] + safety[:-1][:]
    
    person = [False] + person[:-1][:]
    person[n-1] = False

    
def person_move():
    global person
    for i in range(n-2,-1,-1):
        if person[i] :
            if not person[i+1] and safety[i+1] != 0:
                safety[i+1] -= 1
                person[i+1] = True
                person[i] = False

    person[n-1] = False

def person_add():

    if not person[0] and safety[0] != 0 :

        person[0] = True
        safety[0] -= 1

def check_safety():
    cnt = 0
    for i in safety :
        if i == 0 :
            cnt += 1
    if cnt >= k :
        return False
    else :
        return True


exp = 1
while True:

    shift_right()
    person_move()
    person_add()

    if not check_safety():
        break
    else:
        exp += 1
print(exp)
n, k = list(map(int,input().split()))

safety = list(map(int,input().split()))

person = [False for _ in range(2 * n)]


def shift_right():
    global safety,person

    temp = safety[-1]
    safety = [temp] + safety[:-1][:]
    
    person = [False] + person[:-1][:]
    person[n-1] = False

    
def person_move():
    global person
    for i in range(n-2,-1,-1):
        if person[i] :
            if not person[i+1] and safety[i+1] != 0:
                safety[i+1] -= 1
                person[i+1] = True
                person[i] = False

    person[n-1] = False

def person_add():

    if not person[0] and safety[0] != 0 :

        person[0] = True
        safety[0] -= 1

def check_safety():
    cnt = 0
    for i in safety :
        if i == 0 :
            cnt += 1
    if cnt >= k :
        return False
    else :
        return True


exp = 1
while True:

    shift_right()
    person_move()
    person_add()

    if not check_safety():
        break
    else:
        exp += 1
print(exp)
