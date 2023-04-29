# Merge SORT 구현해보기

# def merge_sort(arr):

#     if len(arr) < 2 : # 한개는 정렬된 상태
#         return arr
    
#     mid = len(arr) // 2
#     low_arr,high_arr = merge_sort(arr[:mid]), merge_sort(arr[mid:])
#     merged_arr = [] # merge 해서 차례대로 나열할 빈 리스트
#     l,h = 0,0 # 사실상 투포인터
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merged_arr.append(low_arr[l])
#             l += 1
#         else :
#             merged_arr.append(high_arr[h])
#             h += 1
#     if h == len(high_arr):
#         merged_arr += low_arr[l:]
#     elif l == len(low_arr):
#         merged_arr += high_arr[h:]
    
#     return merged_arr

arr = [34,5,3,2,6,72,34,5,46,7,85,3]

def merge_sort(arr):
    
    if len(arr) < 2 :
        return arr
    mid = len(arr) // 2
    
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    
    l,h = 0,0
    merged_lst = []
    while l < len(low_arr) and h < len(high_arr):
        
        if low_arr[l] <= high_arr[h]:
            merged_lst.append(low_arr[l])
            l += 1
        else :
            merged_lst.append(high_arr[h])
            h += 1
            
    merged_lst += low_arr[l:]
    merged_lst += high_arr[h:]
    
    return merged_lst
        

print(merge_sort(arr))
