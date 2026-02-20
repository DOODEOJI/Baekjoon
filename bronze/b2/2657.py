import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    i, text = map(str, sys.stdin.readline().rstrip().split(" "))
    final = ""
    for t in text:
        final += t*int(i)
    print(final)