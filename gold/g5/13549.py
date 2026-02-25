import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())

bitmap = [0 for _ in range(100002)]
dq = deque()
dq.appendleft((n, 0))

while True:
    current, level = dq.popleft()
    if bitmap[current]:
        continue
    bitmap[current] = 1

    if current == k:
        print(level)
        break
    
    if current + 1 < 100002:
        dq.append((current + 1, level + 1))
    
    if current - 1 >= 0:
        dq.append((current - 1, level + 1))
    
    if current * 2 < 100002:
        dq.appendleft((current * 2, level))