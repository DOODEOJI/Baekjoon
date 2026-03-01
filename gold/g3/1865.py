# 음수 사이클의 유무만 확인하면 되므로 기존 벨만 포드와는 다르게
# 기본 값을 0으로 초기화하고 음수 무한대로 향하는지만 확인

# 기존 벨만포드는 시작점이 아닌 다른 정점의 dist 값은 무한대로 초기화
# for edges 문에서 if dist[current] != INF 조건을 덧붙여야함 (이웃을 하나씩 추가하는 효과)

import sys

TC = int(sys.stdin.readline().rstrip())

def bf():
    dist = [0 for _ in range(N)]

    for i in range(N):
        for j in edges:
            current = j[0]
            next_node = j[1]
            weight = j[2]

            if dist[next_node] > dist[current] + weight:
                dist[next_node] = dist[current] + weight
                if i == N-1:
                    return True
    return False


for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().rstrip().split(" "))
    edges = []

    for _ in range(M):
        s, e, t = map(int, sys.stdin.readline().rstrip().split(" "))
        edges.append((s-1, e-1,t))
        edges.append((e-1, s-1,t))

    for _ in range(W):
        s, e, t = map(int, sys.stdin.readline().rstrip().split(" "))
        edges.append((s-1, e-1, -1*t))

    negative_cycle = bf()
    
    if negative_cycle:
        print("YES")

    else:
        print("NO")
        