import sys

class Set:
    def __init__(self):
        self.set = [0 for i in range(20)]

    def add(self, x):
        self.set[x-1] = 1

    def remove(self, x):
        self.set[x-1] = 0

    def check(self, x):
        print(self.set[x-1])
    
    def toggle(self, x):
        if self.set[x-1]:
            self.set[x-1] = 0
        else:
            self.set[x-1] = 1

    def all(self):
        self.set = [1 for i in range(20)]

    def empty(self):
        self.set = [0 for i in range(20)]

x = Set()

command = {
    "add" : x.add,
    "remove" : x.remove,
    "check" : x.check,
    "toggle" : x.toggle,
    "all" : x.all,
    "empty" : x.empty
}

it = int(str(sys.stdin.readline().rstrip('\n')))

for i in range(it):
    text = sys.stdin.readline().rstrip('\n')
    new = text.split()
    if text == new[0]:
        command[text]()

    else:
        command[new[0]](int(new[1]))