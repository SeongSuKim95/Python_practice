N = int(input())
words = set()

for _ in range(N):
    words.add(input())

words = sorted(words,key = lambda x : (len(x),x))

for word in words:
    print(word)