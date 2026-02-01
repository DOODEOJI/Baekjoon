import sys

word = sys.stdin.readline().rstrip()
alphabet = [-1 for _ in range(26)]

for i in range(len(word)):
    if alphabet[ord(word[i]) - 97] == -1:
        alphabet[ord(word[i]) - 97] = i

print(*alphabet)