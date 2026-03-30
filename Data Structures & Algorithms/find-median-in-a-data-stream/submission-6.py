class MedianFinder:

    def __init__(self):
        # Small = Max Heap
        self.small = []

        # Large = Min Heap
        self.large = []
    

    def addNum(self, num: int) -> None:
        # Add to small 
        heapq.heappush(self.small, -1 * num)

        # Make sure all elems in small < all elems in large 
        if (self.small and self.large and 
            (-1 * self.small[0]) > self.large[0]):
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        # Small > Large
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))

        # Large > Small
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        # Small > Large (by 1)
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2
        