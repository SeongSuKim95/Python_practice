import re
while 1:
    s=input()
    if s=='end':break
    case1 = len(re.findall('[aeiou]',s)) != 0
    case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}',s))==0
    case3 = len(re.findall('[a-df-np-z]\\1',s))==0 # 두번 반복된 케이스를 의미
    if case1 and case2 and case3:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')

# 정규식으로 동일한 문자 n회 반복 찾기
pattern = "[a-zA-Z0-9]\\1{n-1,}"  #참조때문에 이렇게 n-1번 반복 시켜야함!!
while 1:
    s=input()
    if s=='end':break
    case1 = len(re.findall('[aeiou]',s)) != 0
    case2 = len(re.findall('[aeiou]{3}|[^aeiou]{3}',s))==0
    case3 = len(re.findall('([a-df-np-z])\\1',s))==0 # 이미 두번 반복된 케이스를 의미
    if case1 and case2 and case3:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')
