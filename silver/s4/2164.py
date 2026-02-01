import sys

n = int(sys.stdin.readline().rstrip())

n_list = [i for i in range(1, n+1)]
flip = len(n_list) % 2

while (len(n_list) > 1):
    n_list = [n_list[i] for i in range(1, len(n_list), 2)]
    if flip:
        temp = n_list.pop(0)
        n_list.append(temp)
    flip = len(n_list) % 2

print(*n_list)


