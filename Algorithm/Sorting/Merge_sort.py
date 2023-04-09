def merge_sort(arr):
    
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
            
    # 남은 데이터를 밀어 넣어주기
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]

    return merged_arr

arr = [1,3,4,5,3,46,67,7,2,3]
print(merge_sort(arr))
