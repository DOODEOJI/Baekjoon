import sys
import math

num = sys.stdin.readline().rstrip()
num_list = []
bucket = [0 for i in range(10)]

for n in num:
    num_list.append(int(n))
    if n == '9':
        bucket[6] += 1
    else:
        bucket[int(n)] += 1

sum = 0
osum = 0

bucket[6] = math.ceil(bucket[6] / 2)

print(max(bucket))