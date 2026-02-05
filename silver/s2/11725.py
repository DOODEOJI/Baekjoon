import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.connected = []
        self.parent = None

    def __repr__(self):
        return f"{self.parent}"

n = int(sys.stdin.readline().rstrip())
nodes = [Node(v) for v in range(1, n+1)]

for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    nodes[x-1].connected.append(nodes[y-1])
    nodes[y-1].connected.append(nodes[x-1])

process = [nodes[0]]
nodes[0].parent = 0

while process:
    p = process.pop(0)
    for i in p.connected:
        if i.parent is None: # visited 사용하면 O(N) 증가하므로 parent 이용하면 됨           
            process.append(i)
            i.parent = p.value

for n in nodes[1:]:
    print(n)
