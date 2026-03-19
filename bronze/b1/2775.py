import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    apt = []
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    for i in range(k+1):
        apt.append([])
        for j in range(1, n+1):
            if i == 0:
                apt[i].append(j)
            else:
                apt[i].append(sum(apt[i-1][:j]))

    print(apt[-1][-1])
