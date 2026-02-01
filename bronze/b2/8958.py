import sys
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    problems = sys.stdin.readline().rstrip()
    psum = 0
    final = 0
    for p in problems:
        if p == "O":
            psum += 1
            final += psum
        else:
            psum = 0
    print(final)