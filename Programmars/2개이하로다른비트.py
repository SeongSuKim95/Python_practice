def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:]) 

        idx = ''.join(bin_number).rfind('0')    
        
        bin_number[idx] = '1'
        
        if number % 2 == 1:
            bin_number[idx+1] = '0'
        
        answer.append(int(''.join(bin_number), 2))

    return answer

# 2진법으로 바꾸는 방법 : bin(number)[2:]
# list로 바꿔주는 이유는 str을 idx로 접근하여 바꿔주기 위함
# rfind--> str의 오른쪽에서부터 해당 string 찾기, str에 써야하기 때문에 ''.join(bin_number)를 통해 list를 다시 str로 바꿔준 모습
# int(이진수,2)를 통해 2진수를 10진수로 바꿔줄수있음
