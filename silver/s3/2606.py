import sys

class Vertex:
    def __init__(self, index):
        self.index = index
        self.connected = []

n = int(sys.stdin.readline().rstrip())

v_list = [Vertex(i) for i in range(1, n+1)]

l = int(sys.stdin.readline().rstrip())

for _ in range(l):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    v_list[a-1].connected.append(v_list[b-1])
    v_list[b-1].connected.append(v_list[a-1])

p_list = [v_list[0]]
visited = []

while (p_list):
    v = p_list.pop()
    if v.index in visited:
        continue
    else:
        visited.append(v.index)

    for i in v.connected:
        p_list.append(i)

print(len(visited)-1)