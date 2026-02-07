import sys

# DFS 버전
class Tree:
    def __init__(self, value):
        self.root = value
        self.sum = 0
        self.one = None
        self.two = None
        self.three = None

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    t= Tree(0)

    process_list = []
    cnt = 0
    process_list.append(t)
    t.sum = 0

    while process_list:
        p = process_list.pop(0)
        
        if p.sum == n:
            cnt += 1
            continue
        
        if p.sum + 1 <= n:
            p.one = Tree(p.root + 1)
            p.one.sum = p.sum + 1
            process_list.append(p.one)
        
        if p.sum + 2 <= n:
            p.two = Tree(p.root + 2)
            p.two.sum = p.sum + 2
            process_list.append(p.two)

        if p.sum + 3 <= n:
            p.three = Tree(p.root + 3)
            p.three.sum = p.sum + 3
            process_list.append(p.three)

    print(cnt)

# DP 버전

T = int(sys.stdin.readline().rstrip())
dp = [0, 1, 2, 4]

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    for i in range(4, n+1):
        if i < len(dp):
            continue
        dp.append(dp[i-3]+dp[i-2]+dp[i-1])

    print(dp)