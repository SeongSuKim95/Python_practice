def solution(n, arr1, arr2):
    answer = []
    pattern = [" ","#"]
    for i in range(n):
        a1 = bin(arr1[i])[2:].zfill(n)
        a2 = bin(arr2[i])[2:].zfill(n) 
        temp = ''
        for j in range(n):
            temp += pattern[int(int(a1[j]) or int(a2[j]))]
        answer.append(temp)
    return answer


# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer


# import re

# def solution(n, arr1, arr2):
#     answer = ["#"]*n
#     for i in range(0, n):
#         answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
#         answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
#         answer[i] = re.sub('0', ' ', answer[i])
#     return answer