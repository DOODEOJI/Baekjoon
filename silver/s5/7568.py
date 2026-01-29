import sys

class Person:
    def __init__(self, w, h, i):
        self.weight = w
        self.height = h
        self.index = i
        self.rank = None
    
    def __repr__(self):
        return f"{self.rank}"

num = int(str(sys.stdin.readline().rstrip()))
person_list = []

for i in range(num):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    p = Person(w, h, i)
    person_list.append(p)


for i in person_list:
    cnt = 0
    for j in person_list:
        if i.weight < j.weight and i.height < j.height:
            cnt += 1
    i.rank = cnt + 1

print(*person_list)