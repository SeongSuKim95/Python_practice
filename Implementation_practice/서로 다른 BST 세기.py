# DP

n = int(input())

UNUSED = -1

memo = [UNUSED for _ in range(n + 1)]

def get_num_of_unique_bst(n):
    if memo[n] != UNUSED:
        return memo[n]
    
    if n <= 1:
        return 1
    
    number_of_unique_bst = 0
    for i in range(n):
        number_of_unique_bst += get_num_of_unique_bst(i) * \
                                get_num_of_unique_bst(n - i - 1)
        
    memo[n] = number_of_unique_bst
    return memo[n]

print(get_num_of_unique_bst(n))