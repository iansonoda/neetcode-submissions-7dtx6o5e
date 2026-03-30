class MedianFinder:

    def __init__(self):
        # Heaps in python are all min heaps. Multiply by -1 to make max heap.
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        # make sure ever num in small is <= every num in large
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):

            temp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, temp)

        # uneven size, small > large + 1
        if len(self.small) > len(self.large) + 1:
            temp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, temp)

        # uneven size, large > small + 1
        if len(self.large) > len(self.small) + 1:
            temp = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, temp)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (self.large[0] + (-1 * self.small[0])) / 2





