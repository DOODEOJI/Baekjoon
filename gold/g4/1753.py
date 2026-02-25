import sys
import heapq

class Vertex:
    def __init__(self, name):
        self.name = name
        self.out_edge = []

class Edge:
    def __init__(self, end, value):
        self.end = end
        self.value = value

v, e = map(int, sys.stdin.readline().rstrip().split(" "))
start = int(sys.stdin.readline().rstrip())

distance = [111111111 for i in range(v)]
distance[start-1] = 0

vertex_list = []

for j in range(1, v+1):
    vertex_list.append(Vertex(j))

for _ in range(e):
    u, vertex, w = map(int, sys.stdin.readline().rstrip().split(" "))
    edge = Edge(vertex, w)
    vertex_list[u-1].out_edge.append(edge)

heap = [(0, start-1)]

while heap:
    min_distance, min_idx = heapq.heappop(heap)

    if min_distance > distance[min_idx]:
        continue
    min_vertex = vertex_list[min_idx]

    for j in min_vertex.out_edge:
        if min_distance + j.value < distance[j.end-1]:
            distance[j.end-1] = min_distance + j.value
            heapq.heappush(heap, (min_distance + j.value, j.end-1))

dist = [d if d != 111111111 else "INF" for d in distance]
print("\n".join(map(str, dist)))