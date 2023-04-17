from itertools import product
def solution(word):
    answer = 0
    alpha = ['A','E','I','O','U']
    word_list = []
    
    for i in range(1,6):
        temp = list(product(alpha,repeat = i))
        for words in temp:
            word_list.append(''.join(words))
    answer = sorted(word_list).index(word) + 1
    return answer


# 중복을 허용한 permutations : product(list,repeat = i)
# 중복을 허용한 combinations : combination_with_replacement(list, num)