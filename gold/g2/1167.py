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

for _ in range(n):
    c = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    p = c.pop(0)
    temp = []
    for i in c:
        if i == -1:
            break
        if temp:
            temp.append(i)
            tree[p-1].append((temp[0]-1,temp[1]))
            temp = []
        else:
            temp.append(i)

max_node = 0
for _ in range(2):
    max_value = 0
    dfs(max_node, max_value, -1)

print(max_value)