import sys

def merge_sort(arr):
    
    if len(arr) < 2 :
        return arr

    mid = len(arr) // 2

    low_arr , high_arr = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    l = h = 0
    merged_lst = []
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_lst.append(low_arr[l])
            l += 1
        else :
            merged_lst.append(high_arr[h])
            h += 1
    
    if l == len(low_arr):
        merged_lst += high_arr[h:]
    elif h == len(high_arr):
        merged_lst += low_arr[l:]
    
    return merged_lst

    
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))

merged_lst = merge_sort(lst)

for i in merged_lst:
    print(i)