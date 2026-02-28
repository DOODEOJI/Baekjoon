import sys 

n = int(sys.stdin.readline().rstrip())
score = list(map(int, sys.stdin.readline().rstrip().split(" ")))
max_score = max(score)

print((sum(score)*100/max_score)/n)