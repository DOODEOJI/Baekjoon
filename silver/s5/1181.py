import sys

n = int(sys.stdin.readline().rstrip())
word = {}

for _ in range(n):
    w = sys.stdin.readline().rstrip()
    if len(w) in word:
        word[len(w)].append(w)
    else:
        word[len(w)] = [w]

word_dict = sorted(word.items())

for i, word in word_dict:
    sort_list = sorted(list(set(word)))

    for word in sort_list:
        print(word)