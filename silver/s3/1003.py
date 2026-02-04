import sys

def process(t):
    if t in memo:
        zero_and_one[0] += memo[t][1]
        zero_and_one[1] += memo[t][2]
        return memo[t][0]

    if t == 0:
        zero_and_one[0] += 1
        return 0
    
    elif t == 1:
        zero_and_one[1] += 1
        return 1
    
    else:
        memo[t] = process(t-1) + process(t-2)
        memo[t] = [memo[t], zero_and_one[0], zero_and_one[1]]

    return memo[t][0]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    memo = {}
    zero_and_one = {
        0 : 0,
        1: 0
    } 
    k = int(sys.stdin.readline().rstrip())
    process(k)
    print(zero_and_one[0], zero_and_one[1])