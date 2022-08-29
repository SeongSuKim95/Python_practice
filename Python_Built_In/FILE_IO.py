#open(): 읽을 때 r, 쓸 때 w
#read(): 파일의 모든 내용을 읽음
f = open("input.txt","r")

# a= []
# for i in range(10):
#     line = []
#     for j in range(10):
#         line.append(10*i+j)
#     a.append(line)

print(f.read())
#f.seek(9) # 9 byte의 위치부터 file을 읽음 한글은 글자당 3byte alpha,기호 1byte
#readlines(): 전체 내용을 한 번에 리스트에 담는 함수
count = 0
# list = f.readlines()
# print(list)
#
# for i, data in enumerate(list):
#     print("%d번째 줄 : %s" %(i+1, data), end = '')

while count <3:
    data = f.readline() # 줄마다 처리
    count = count+1
    print("%d번째 줄: %s" %(count,data), end = '')

f.close()

with open("input.txt", "r") as f:
    list = f.readlines()
    for i, data in enumerate(list):
        print("%d번째 줄: %s" %(i+1,data), end= '')

def process(filename):

    with open(filename,"r") as f:
        dict = {}
        data = f.read()
        for i in data:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        return dict

dict = process("input.txt")
dict = sorted(dict.items(), key = lambda a:a[1], reverse =True) # 내림차순 정렬

for data, count in dict: # dict 자료형: list
    if data == '\n' or data == ' ':
        continue
    print("%d번 출현: [%c]" %(count,data))

print(dict)