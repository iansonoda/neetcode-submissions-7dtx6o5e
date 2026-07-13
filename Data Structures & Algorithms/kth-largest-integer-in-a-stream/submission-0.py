class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_heap = []

        for num in nums:
            if len(self.k_heap) < k:
                heapq.heappush(self.k_heap, num)

            else:
                heapq.heappushpop(self.k_heap, num)
        
    def add(self, val: int) -> int:
        if len(self.k_heap) < self.k:
            heapq.heappush(self.k_heap, val)

        else:
            heapq.heappushpop(self.k_heap, val)

        return self.k_heap[0]