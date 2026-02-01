import sys

n = int(sys.stdin.readline().rstrip())

n_dict = {}

n_list = map(int, sys.stdin.readline().rstrip().split(' '))

for num in n_list:
    if num not in n_dict.keys():
        n_dict[num] = 0
    n_dict[num] += 1

m = int(sys.stdin.readline().rstrip())

final_list = []
n2_list = map(int, sys.stdin.readline().rstrip().split(' '))
dict_list = n_dict.keys()

for num in n2_list:
    if num in dict_list:
        final_list.append(n_dict[num])
    else:
        final_list.append(0)

print(*final_list)