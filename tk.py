num = int(input())
name = input()
pattern = input()

words = name.split()
num_words = len(words)

count = 0
last = ''
for word in words:
    l = len(word)
    for i in range(l):
        if i == 0:
            last = pattern[i]
            continue
        if pattern[i] == last:
            count += 1
