import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))

n_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
sum_list = []

nsum = 0
sum_list.append(0)
for num in n_list:
    nsum += num
    sum_list.append(nsum)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split(" "))
    print(sum_list[j] - sum_list[i-1])