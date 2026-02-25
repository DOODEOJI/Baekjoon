import sys
sys.setrecursionlimit(10**7)

def dfs(node, weighted_sum, prev):
    global max_value, max_node

    if max_value < weighted_sum:
        max_value = weighted_sum
        max_node = node
    
    for i in tree[node]:
        if i[0] == prev:
            continue
        dfs(i[0], weighted_sum + i[1], node)

n = int(sys.stdin.readline().rstrip())

tree = [[] for _ in range(n)]

for _ in range(n-1):
    p, c, w = map(int, sys.stdin.readline().rstrip().split(" "))
    tree[p-1].append((c-1,w))
    tree[c-1].append((p-1,w))

max_node = 0
for _ in range(2):
    max_value = 0
    dfs(max_node, max_value, -1)

print(max_value)