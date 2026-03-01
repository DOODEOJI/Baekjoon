import sys

n = int(sys.stdin.readline().rstrip())
bus = int(sys.stdin.readline().rstrip())

bus_map = [[0 if i == j else 10**10 for i in range(n)] for j in range(n)]

for b in range(bus):
    s, e, w = map(int, sys.stdin.readline().rstrip().split(" "))
    bus_map[s-1][e-1] = min(bus_map[s-1][e-1], w)

for k in range(n):
    for i in range(n):
        if i == k:
            continue
        
        for j in range(n):
            if j == k or j == i:
                continue
            candidate = bus_map[i][k] + bus_map[k][j]
            if candidate < bus_map[i][j]:
                bus_map[i][j] = candidate

for row in bus_map:
    for idx in range(n):
        if row[idx] == 10**10:
            row[idx] = 0
    print(*row)