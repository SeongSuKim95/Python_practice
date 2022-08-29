# def solution(dartResult):
#     answer = 0
#     cnt = 0
#     num,bonus,opt = ['']*3,[0]*3,['']*4
#     bonus_dict = {"S":1,"D":2,"T":3}
#     flag = False
#     for i in dartResult:
#         if i.isdigit():
#             num[cnt] += i
#             flag = True
#         if not i.isdigit() and flag:
#             if i in bonus_dict:
#                 bonus[cnt] = bonus_dict[i]
#             cnt += 1
#             flag = False
#         if i in ["*","#"]:
#             opt[cnt] = i
#     opt_num = [1] * 4
#     for idx,i in enumerate(opt[1:]):
#         if i == "*":
#             opt_num[idx-1] *= 2
#             opt_num[idx] *= 2
#         elif i == "#":
#             opt_num[idx] *=-1
            
#     print(num,bonus,opt,opt_num)
#     for i in range(3):
#         answer += int(num[i])**bonus[i]*opt_num[:-1][i]
#     return answer

import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

# 규칙 찾기 (정규식 표현)