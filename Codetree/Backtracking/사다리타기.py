# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))

lines = list()
selected_lines = list()

ans = m

# 처음 상황과, 선택한 가로줄만 사용했을 때의
# 상황을 시뮬레이션하여
# 둘의 결과가 같은지 확인합니다.
def possible():
    # Step1. 시작 숫자를 셋팅합니다.
    num1, num2 = [i for i in range(n)], [i for i in range(n)]
	
    # Step2. 위에서부터 순서대로 적혀있는 
    # 가로줄에 대해 양쪽 번호에 해당하는 숫자를 바꿔줍니다. 
    for _, idx in lines:
        num1[idx], num1[idx + 1] = num1[idx + 1], num1[idx]
    for _, idx in selected_lines:
        num2[idx], num2[idx + 1] = num2[idx + 1], num2[idx]
	
    # Step3. 두 상황의 결과가 동일한지 확인합니다.
    for i in range(n):
        if num1[i] != num2[i]:
            return False

    return True


def find_min_lines(cnt):
    global ans
    
    if cnt == m:
        if possible():
            ans = min(ans, len(selected_lines))
        return
    
    selected_lines.append(lines[cnt])
    find_min_lines(cnt + 1)
    selected_lines.pop()
	
    find_min_lines(cnt + 1)


for _ in range(m):
    a, b = tuple(map(int, input().split()))
    lines.append((b, a - 1))

lines.sort()

find_min_lines(0)
print(ans)