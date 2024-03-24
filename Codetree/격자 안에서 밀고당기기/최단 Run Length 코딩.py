string = input()

def shiftRightOnce(curString):
    strList = list(curString)
    last = strList[-1]
    for i in range(len(strList)-2,-1,-1):
        strList[i+1] = strList[i]
    strList[0] = last
    return ''.join(strList)

def getRunLength(string):

    # 앞에서 부터 차례대로 다음 문자와 일치하는지 확인
    curStr,curCnt, runLength = string[0],1, string[0]
    for i in range(1,len(string)):
        if string[i] == curStr:
            curCnt += 1
        else :
            curStr = string[i]
            runLength += str(curCnt)+curStr
            curCnt = 1
    runLength += str(curCnt)
    return len(runLength)

def solve():
    global string
    answer = 1e9
    for i in range(len(string)):     
        string = shiftRightOnce(string)
        answer = min(answer,getRunLength(string))
    print(answer)

solve()
        
