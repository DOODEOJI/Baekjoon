import sys
import heapq

def dijkstra(idx, start):
    dist = [10**10 for _ in range(n)]
    dist[idx] = 0
    heap = [(0, idx)]
    heapq.heapify(heap)
    while heap:
        d, idx = heapq.heappop(heap)
        if d > dist[idx]:
            continue

        if idx == x-1 and not start:
            return d

        for j in range(n):
            if dist[idx] + dijk[idx][j] < dist[j]:
                dist[j] = dist[idx] + dijk[idx][j]
                heapq.heappush(heap, (dist[j], j))
    
    return dist

n, m, x = map(int, sys.stdin.readline().rstrip().split(" "))

dijk = [[0 if i == j else 10**5 for i in range(n)] for j in range(n)]
max_dist = 0

for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().rstrip().split(" "))
    dijk[a-1][b-1] = t

go = dijkstra(x-1, True)

for i in range(n):
    if i == x-1:
        continue
    candidate = dijkstra(i, False) + go[i]
    if max_dist < candidate:
        max_dist = candidate

print(max_dist)