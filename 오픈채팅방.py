#이정도는 풀수있구만,,,

def solution(record):
    answer = []
    ID_name = {}
    ID_inout = {}
    for idx,i in enumerate(record):
        temp = i.split(' ')
        if len(temp) == 3:
            action,ID,name = temp[0], temp[1],temp[2]
            if action == "Enter" :
                ID_name[ID] = name
                ID_inout[idx] = ID
            else :
                ID_name[ID] = name
        else :
            ID = temp[1]
            ID_inout[-idx] = ID
    for idx,ID in ID_inout.items():
        if idx >= 0 :
            answer.append(f"{ID_name[ID]}님이 들어왔습니다.")
        else:
            answer.append(f"{ID_name[ID]}님이 나갔습니다.")
                          
    return answer