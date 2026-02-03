import sys

memo = {}

def process(t):
    if t in memo:
        return memo[t]

    if t == 0:
        return 0
    
    elif t == 1:
        return 1
    
    elif t == 2:
        return 2
    
    else:
        memo[t] = process(t-1) + process(t-2)

    return memo[t]

n = int(sys.stdin.readline().rstrip())
k = process(n) % 10007

print(k)