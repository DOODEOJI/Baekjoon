import sys

chess = sys.stdin.readline().rstrip().split()

right = [1, 1, 2, 2, 2, 8]

index = 0
right_str = ''

for i in chess:
    right_str = right_str + str(right[index] - int(i)) +" "
    index += 1

print(right_str.rstrip())