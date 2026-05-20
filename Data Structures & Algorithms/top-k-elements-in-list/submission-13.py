class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, count in count.items():
            if len(res) == k:
                heapq.heappushpop(res, (count, num))
            else:
                heapq.heappush(res, (count, num))

        result = [num for (count, num) in res]

        return result