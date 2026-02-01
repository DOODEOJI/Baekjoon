import sys
n = int(sys.stdin.readline().rstrip())

n_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

print(min(n_list), max(n_list))