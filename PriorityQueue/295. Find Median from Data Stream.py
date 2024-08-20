import bisect
# bisect module inserts elem in list in sorted order O(n) rather than sorting the list each time we append i.e O(n logn)
class MedianFinder:

    def __init__(self):
        self.obj = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.obj, num)

    def findMedian(self) -> float:
        n = len(self.obj)
        if n == 1:
            return float(self.obj[0])
        elif n % 2 == 0:
            return (self.obj[n // 2] + self.obj[n // 2 - 1]) / 2
        else:
            return float(self.obj[n // 2])
