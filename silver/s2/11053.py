import sys

num = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

dp = [1 for _ in range(num)]

for i in range(1, num):
    best = 0
    for j in range(i-1, -1, -1):
        if n_list[i] > n_list[j]:
            if best < dp[j]:
                best = dp[j]

    if best == 0:
        continue

    dp[i] = best + 1

print(max(dp))