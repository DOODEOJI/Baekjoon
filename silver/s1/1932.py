import sys

n = int(sys.stdin.readline().rstrip())
dp = []

for i in range(n):
    number = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    dp.append(number)

for j in range(n-1, 0, -1):
    temp = []
    for k in range(0 ,j):
        temp.append(max(dp[j][k], dp[j][k+1]))
    for p in range(j):
        dp[j-1][p] = dp[j-1][p] + temp[p]

print(*dp[0])