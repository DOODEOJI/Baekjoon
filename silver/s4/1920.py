import sys

n = int(sys.stdin.readline().rstrip())

n_list = set(map(int, sys.stdin.readline().rstrip().split(' ')))

m = int(sys.stdin.readline().rstrip())

final_list = []
n2_list = map(int, sys.stdin.readline().rstrip().split(' '))

for num in n2_list:
    if num in n_list:
        final_list.append(1)
    else:
        final_list.append(0)

print(*final_list)