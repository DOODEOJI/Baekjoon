import sys

class Vertex:
    def __init__(self, index):
        self.index = index
        self.connected = []

v, e = map(int, sys.stdin.readline().rstrip().split(" "))

v_list = [Vertex(i) for i in range(1, v+1)]

for _ in range(e):
    a, b = map(int, sys.stdin.readline().rstrip().split(" "))
    v_list[a-1].connected.append(v_list[b-1])
    v_list[b-1].connected.append(v_list[a-1])

p_list = [v_list.pop()]
visited = []
connected = 1

while (v_list):
    if p_list: 
        v = p_list.pop()
        if v.index in visited:
            continue
    else:
        v = v_list.pop()
        if v.index in visited:
            continue
        connected += 1
    
    visited.append(v.index)
    for i in v.connected:
        p_list.append(i)

print(connected)