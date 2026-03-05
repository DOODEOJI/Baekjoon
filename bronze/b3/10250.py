import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    h, w, n = map(int, sys.stdin.readline().rstrip().split(" "))
    floor = n % h
    
    if n % h == 0:
        room = n // h
        floor = h
    else:
        room = n // h + 1

    if room < 10:
        room = "0" + str(room)

    print(str(floor)+str(room))