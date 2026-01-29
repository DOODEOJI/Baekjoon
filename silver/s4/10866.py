import sys

class Deque:
    def __init__(self):
        self.deque = []
        self.f = None
        self.b = None

    def push_front(self, x):
        self.deque.insert(0, x)
        self.f = x
        if len(self.deque) == 1:
            self.b = x

    def push_back(self, x):
        self.deque.append(x)
        self.b = x
        if len(self.deque) == 1:
            self.f = x
        
    def pop_front(self):
        if len(self.deque) == 0:
            return -1
        old = self.f
        if len(self.deque) == 1:
            self.f = None
            self.b = None
        else:
            self.f = self.deque[1]
        del self.deque[0]

        return old
    
    def pop_back(self):
        if len(self.deque) == 0:
            return -1
        old = self.b
        self.deque.pop()
        if len(self.deque) == 0:
            self.f = None
            self.b = None
        else:
            self.b = self.deque[-1]
        return old

    def size(self):
        return len(self.deque)
    
    def empty(self):
        if len(self.deque) == 0:
            return 1
        return 0
    
    def front(self):
        if len(self.deque) == 0:
            return -1
        
        return self.f
    
    def back(self):
        if len(self.deque) == 0:
            return -1
        
        return self.b
    
    def __repr__(self):
        return f"{self.deque}"

x = Deque()

command = {
    "push_front" : x.push_front,
    "push_back" : x.push_back,
    "pop_front" : x.pop_front,
    "pop_back" : x.pop_back,
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