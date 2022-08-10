# 내코드
def solution(s):
    stack = []
    answer_len = []
    # 5번 테케 : 문자열 길이가 1일때 ex) "a" --> 1
    if len(s) == 1:
        return 1
    for i in range(1,int(len(s)/2)+1): # step
        answer = ''
        for j in range(0,len(s),i): # fragments
            temp = s[j:j+i]
            # print(stack,temp)
            if not stack:
                cnt = 1
                stack.append(temp)
            else:
                if stack[-1] == temp:
                    cnt +=1
                    # print(cnt)
                else :
                    if cnt >= 2:
                        answer += str(cnt) + stack.pop()
                    else:
                        answer += stack.pop()
                    cnt = 1
                    stack.append(temp)
        if cnt != 1:
            answer += str(cnt) + stack.pop()
        else:
            answer += stack.pop()
        answer_len.append(len(answer))
    return min(answer_len)

# 정답 코드

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
