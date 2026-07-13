class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
            dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(min_heap, (-dist, point))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = [point for (_, point) in min_heap]
        return res