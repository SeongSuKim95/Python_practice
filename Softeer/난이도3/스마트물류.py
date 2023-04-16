N, K = list(map(int,input().split()))

lines = list(input())


def can_catch(H,P):

    return P - K <= H or H <= P + K

def in_range(x):

    return 0<=x<N

catched = [False] * N
answer = 0
for idx,elem in enumerate(lines):
    if elem == "P":
        for h_idx in range(idx-K,idx+K+1):
            if in_range(h_idx):
                if lines[h_idx] == "H" and not catched[h_idx]:
                    catched[h_idx] = True
                    answer += 1
                    break
print(answer)
# H,P = [],[]

# for idx,elem in enumerate(lines):
#     if elem == "H":
#         H.append(idx)
#     else :
#         P.append(idx)

# H_pos = 0
# answer = 0
# for P_pos in P:
#     while H[H_pos] <= P_pos + K :
#         if can_catch(H[H_pos],P_pos):
#             answer += 1
#             H_pos += 1
#             break
#         H_pos += 1
# print(answer)