string = input()
string_r = string[::-1]

def check():
    for i in range(len(string)):
        if string[i] != string_r[i]:
            return 0
    return 1

print(check())
