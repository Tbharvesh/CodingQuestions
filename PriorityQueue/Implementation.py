
# Method-1
print("Method 1 ~ Using heapq Module")
import heapq
pq = []

# Priorities are by default in asc order i.e MIN HEAP
# heapq.heappush(pq , 4)
# heapq.heappush(pq , 1)
# heapq.heappush(pq ,2)

# Task associated with priority
heapq.heappush(pq , (2,'a'))
heapq.heappush(pq , (1,'b'))
heapq.heappush(pq , (3,'c'))

while pq:
    priority , task = heapq.heappop(pq)
    print(f"Task: {task}, Priority: {priority}")
    
# Method 2
print("Method 2 ~ using queue.PriorityQueue Class ")
import queue
pq = queue.PriorityQueue()

pq.put((2,'a'))
pq.put((1,'b'))
pq.put((4,'c'))

while not pq.empty():
    priority , task = pq.get()
    print(f"Task: {task}, Priority: {priority}")
    
# Method 3
print("Method 3 ~ Using a Custom Implementation with a Sorted List")
class PriorityQ:
    def __init__(self):
        self.queue = []
    def insert(self, priority , task):
        # Insert every priority / elem in list
        self.queue.append((priority , task))
        # Sort the list every time you insert an elem 
        # So as tpo maintain the MIN heap property
        self.queue.sort()
    def pop(self):
        
        return self.queue.pop(0)
    
pq = PriorityQ()
pq.insert(2,'a')
pq.insert(1,'b')
pq.insert(3,'c')

while pq.queue :
    priority , task = pq.pop()
    print(f"Task: {task}, Priority: {priority}")
    

        