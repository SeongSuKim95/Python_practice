def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(10))