import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))

bag = [0 for _ in range(k+1)]

for i in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split(" "))
    for j in range(k, w-1, -1):
        bag[j] = max([bag[j-w]+v, bag[j]])

print(bag[-1])