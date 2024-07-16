# Intuition : 

# Method 1 PriorityQ

import heapq

class SmallestInfiniteSet: # type: ignore
    def __init__(self):
        self.heap = []
        self.set = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.set.remove(smallest)
            return smallest
        else:
            result = self.smallest
            self.smallest += 1
            return result

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.set:
            heapq.heappush(self.heap, num)
            self.set.add(num)
            
# Method2 _ sets
class SmallestInfiniteSet:
    def __init__(self):
        self.set = set()
        self.cur = 1 # cur stores the current smallest elem

    def popSmallest(self) -> int:
        # If set is non empty ---> means set has val s.t val<cur so we will remove the min(set) value
        if self.set:
            res = min(self.set)
            self.set.remove(res)
            return res
        else:
            self.cur += 1
            return self.cur - 1
        
    def addBack(self, num: int) -> None:
        # If cur>val to be added , add num in set 
        #else : the cur will already be stored while cur+=1 in pop() func
        # if num < self.cur : DONT TAKE THIS Bcoz already covereed in pop()
        if self.cur > num:
            self.set.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
param_1 = obj.popSmallest()
obj.addBack(num)