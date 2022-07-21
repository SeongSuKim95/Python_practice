from collections import Counter
def solution(str1, str2):
    answer = 0
    
    str1_tmp,str2_tmp = ' '+str1 ,' '+str2
    str1_comb, str2_comb = [],[]
    for a,b in zip(str1_tmp,str1):
        if (a+b).isalpha():
            tmp = (a+b).lower()
            str1_comb.append(tmp)

    for c,d in zip(str2_tmp,str2):
        if (c+d).isalpha():
            tmp = (c+d).lower()
            str2_comb.append(tmp)
    str1_cnt,str2_cnt = Counter(str1_comb),Counter(str2_comb)
    
    inter = list((str1_cnt & str2_cnt).elements())
    union = list((str1_cnt | str2_cnt).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else :
        return int(len(inter)/len(union) * 65536)


test1 = [1,1,2,2,3,3,3]
test2 = [2,2,3,3,3]

x = (Counter(test1) & Counter(test2)).elements()

for i in x:
    print(i)