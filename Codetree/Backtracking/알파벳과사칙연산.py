string = list(input())
alphaSet = set()
signs = []
for i in string:
    if i.isalpha():
        alphaSet.add(i)
    else :
        signs.append(i)

alphas = list(alphaSet)
N = len(alphaSet)
selectedNum = []
answer = -1e9

def calculate():
    alphaNumMap = {}
    for alpha,num in zip(alphas,selectedNum):
        alphaNumMap[alpha] = num
    curValue, curSign = alphaNumMap[string[0]], ''
    for curStr in string[1:]:
        if curStr.isalpha(): # num
            if curSign == "-":
                curValue -= alphaNumMap[curStr]
            elif curSign == "+":
                curValue += alphaNumMap[curStr]
            elif curSign == "*":
                curValue *= alphaNumMap[curStr]
        else : # sign
            curSign = curStr
    return curValue

def selectNum(idx):
    global answer
    if idx == N :
        answer = max(answer,calculate())
        return
    
    for i in range(1,5):

        selectedNum.append(i)
        selectNum(idx+1)
        selectedNum.pop()

selectNum(0)
print(answer)