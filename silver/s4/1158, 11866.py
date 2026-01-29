import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

class Num:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
    def __repr__(self):
        return f"{self.value}"

num_list = [Num(i) for i in range(1,n+1)]

for i in range(len(num_list)):
    if (i+1) >= n:
        num_list[i].prev = num_list[i-1]
        num_list[i].next = num_list[0]

    elif (i-1 < 0):
        num_list[i].prev = num_list[-1]
        num_list[i].next = num_list[i+1]

    else:
        num_list[i].prev = num_list[i-1]
        num_list[i].next = num_list[i+1]

pop_obj = None
next_obj = num_list[0]
pop_list = []

while num_list:
    cnt = k
    pop_obj = next_obj
    while (cnt > 1):
        cnt -= 1
        pop_obj = pop_obj.next

    next_obj = pop_obj.next
    pop_obj.prev.next = pop_obj.next
    pop_obj.next.prev = pop_obj.prev

    pop_list.append(pop_obj)
    num_list.remove(pop_obj)

print(str(pop_list).replace('[', '<').replace(']', '>'))