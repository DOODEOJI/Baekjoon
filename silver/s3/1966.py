import sys

Num = int(sys.stdin.readline().rstrip())

class Queue:
    def __init__(self):
        self.queue = []

    def go_back(self):
        temp = self.queue[0]
        self.queue = self.queue[1:]
        self.queue.append(temp)

for _ in range(Num):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    num_list = sys.stdin.readline().rstrip().split()
    q = Queue()
    for i in num_list:
        q.queue.append(int(i))
    
    q.queue[M] = (q.queue[M],)
    cnt = 0
    while(q.queue):

        found = True
        i = q.queue[0]
        if isinstance(q.queue[0], tuple):
            i_compare = q.queue[0][0]
        else:
            i_compare = q.queue[0]

        for j in q.queue:

            if isinstance(j, tuple):
                j_compare = j[0]
            else:
                j_compare = j
            
            if i_compare < j_compare:
                q.go_back()
                found = False
                break
        
        if found:
            cnt += 1
            if isinstance(i, tuple):
                print(cnt)
                break
            else:
                q.queue.remove(i_compare)