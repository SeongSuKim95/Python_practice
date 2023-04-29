import re, sys
input = sys.stdin.readline
n = int(input())
s,e = input().rstrip().split("*")
pt = re.compile(s+".*"+e+"+")

for i in range(n):
    string = input().rstrip()
    a = pt.search(string)
    if a and a.group() == string: # 처음 찾은게 string과 일치할 경우 --> 즉, 하나만 찾은 패턴이 string이다!
        print("DA")
    else:
        print("NE")