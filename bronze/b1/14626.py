import sys

ISBN = sys.stdin.readline().rstrip()
idx = [1,3,1,3,1,3,1,3,1,3,1,3]
missing = 0
m = ISBN[-1]

isum = 0

for i in range(len(ISBN)-1):
    if ISBN[i] == "*":
        missing = idx[i]
        continue
    isum += (idx[i] * int(ISBN[i]))

for j in range(10):
    if (isum + int(m) + missing * j) % 10 == 0:
        print(j)
