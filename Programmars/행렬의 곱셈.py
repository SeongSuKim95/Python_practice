def solution(arr1, arr2):
    answer = []
    arr2_temp = []
    for i in range(len(arr2[0])):
        temp = []        
        for elements in arr2:
            temp.append(elements[i])
        arr2_temp.append(temp)

    for a in arr1:
        temp = []
        for b in arr2_temp :
            sum = 0
            for i in range(len(a)):
                sum += a[i]*b[i]
            temp.append(sum)
        answer.append(temp)
    return answer