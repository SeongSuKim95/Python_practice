def solution(numbers, hand):
    answer = ''
    num_dict = {10:[0,0],0:[1,0],11:[2,0],7:[0,1],8:[1,1],9:[2,1],4:[0,2],5:[1,2],6:[2,2],1:[0,3],2:[1,3],3:[2,3]} # *:10, #:11
    
    left_num = 10
    right_num = 11
    
    for i in numbers:
        if i in [1,4,7]:
            left_num = i
            answer += "L"
        elif i in [3,6,9]:
            right_num = i
            answer += "R"
        elif i in [2,5,8,0]:
            left_dist = abs(num_dict[i][1] - num_dict[left_num][1]) + abs(num_dict[i][0] - num_dict[left_num][0])
            right_dist = abs(num_dict[i][1] - num_dict[right_num][1]) + abs(num_dict[i][0] - num_dict[right_num][0])
            
            if left_dist > right_dist :
                right_num = i
                answer += "R"
            elif left_dist < right_dist :
                left_num = i
                answer += "L"
            else:
                if hand == "right":
                    right_num = i
                    answer += "R"
                else:
                    left_num = i
                    answer += "L"
                
    return answer

# 유클리디안 distance로 풀면 왜 안될까?
# --> 문제에서 상하좌우로만 이동한다고 써있거든요...