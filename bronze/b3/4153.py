import sys

while True:
    tri = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    if tri[0] == 0:
        break
    
    max_num = max(tri)
    tri.remove(max_num)

    tsum = 0

    for n in tri:
        tsum += (n ** 2)

    if max_num ** 2 == tsum:
        print("right")
    else:
        print("wrong")