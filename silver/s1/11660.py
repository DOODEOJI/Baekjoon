import sys

n, m = map(int, sys.stdin.readline().rstrip().split(" "))
numbers = []

for _ in range(n):
    n_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    nsum = 0
    new = []
    for n in n_list:
        nsum += n
        new.append(nsum)
    numbers.append(new)

for _ in range(m):
    sx, sy, ex, ey = map(int, sys.stdin.readline().rstrip().split(" "))
    fsum = 0
    for i in range(sx-1, ex):
        if (sy - 2) == -1:
            num = 0
        else:
            num = numbers[i][sy-2]
        fsum += (numbers[i][ey-1] - num)
    print(fsum)