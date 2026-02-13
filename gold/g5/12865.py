import sys

n, k = map(int, sys.stdin.readline().rstrip().split(" "))

bag = [0 for _ in range(k)]

for _ in range(n):
    w, v = map(int, sys.stdin.readline().rstrip().split(" "))
    bag[w-1] = v

for i in range(k):
    max_value = bag[i]
    for j in range(i//2):
        if bag[j] == 0 or bag[i-j-1] == 0:
            continue
        if (bag[j] + bag[i-j-1]) > max_value:
            max_value = bag[j] + bag[i-j-1]

    bag[i] = max_value

print(bag[-1])
