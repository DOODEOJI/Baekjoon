import sys

class Queue:
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        if len(self.stack) == 0:
            return -1
        old = self.stack[0]
        self.stack.pop(0)
        return old
    
    def size(self):
        return len(self.stack)
    
    def empty(self):
        if len(self.stack) == 0:
            return 1
        return 0
    
    def front(self):
        if len(self.stack) == 0:
            return -1
        
        return self.stack[0]

    def back(self):
        if len(self.stack) == 0:
            return -1
        
        return self.stack[-1]


x = Queue()

command = {
    "push" : x.push,
    "pop" : x.pop,
    "size" : x.size,
    "empty" : x.empty,
    "front" : x.front,
    "back" : x.back
}

it = int(str(sys.stdin.readline().rstrip('\n')))

for i in range(it):
    text = sys.stdin.readline().rstrip('\n')
    new = text.split()
    if text == new[0]:
        result = command[text]()

    else:
        result = command[new[0]](new[1])
        
    if result is None:
        continue
    print(result) 