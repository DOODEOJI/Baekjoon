import sys

s1 = sys.stdin.readline().rstrip() 
s2 = sys.stdin.readline().rstrip() 

dp = [0 for _ in range(len(s1)+1)]
idx = [0 for _ in range(len(s1)+1)]

for i in range(len(s1)):
    print(s2[idx[i]:], s1[i])
    idx[i+1] = s2[idx[i]:].find(s1[i])
    if idx[i+1] == -1:
        idx[i+1] = idx[i]
        dp[i+1] = dp[i]
    else:
        dp[i+1] = dp[i] + 1
        idx[i+1] = idx[i] + idx[i+1] + 1

print(dp[-1])