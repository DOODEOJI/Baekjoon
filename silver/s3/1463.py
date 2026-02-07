import sys
n = int(sys.stdin.readline().rstrip())

# DFS 버전
class Tree:
    def __init__(self, value):
        self.root = value
        self.level = None
        self.one = None
        self.two = None
        self.three = None
        
t= Tree(n)

process_list = []
process_list.append(t)
t.level = 0
visited = []

while process_list:
    p = process_list.pop(0)
    if p.root in visited:
        continue
    visited.append(p.root)
    if p.root == 1:
        print(p.level)
        break

    if p.root % 2 == 0:
        p.two = Tree(p.root / 2)
        p.two.level = p.level + 1
        process_list.append(p.two)
    
    if p.root % 3 == 0:
        p.three = Tree(p.root / 3)
        p.three.level = p.level + 1
        process_list.append(p.three)

    p.one = Tree(p.root - 1)
    p.one.level = p.level + 1
    process_list.append(p.one)

# DP 버전
dp = [0]
dp.append(0)

for i in range(2, n+1):
    candidate = []
    if i % 3 == 0:
        candidate.append(dp[i//3] + 1)
    if i % 2 == 0:
        candidate.append(dp[i//2] + 1)
    
    candidate.append(dp[i-1] + 1)

    dp.append(min(candidate))

print(dp[n])