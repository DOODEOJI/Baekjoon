import sys

num = int(str(sys.stdin.readline().rstrip()))
num_list = set()

for i in range(num):
    num = int(str(sys.stdin.readline().rstrip()))
    num_list.add(num)

for i in sorted(list(num_list)):
    print(i)