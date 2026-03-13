import sys

n = int(sys.stdin.readline().rstrip())
count = [0 for _ in range(10000)]

for _ in range(n):
    k = int(sys.stdin.readline().rstrip())
    count[k-1] += 1

for j in range(n):
    if count[j] == 0:
        continue
    for _ in range(count[j]):
        print(j+1)