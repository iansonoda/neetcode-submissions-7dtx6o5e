class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        min_speed = r

        while l <= r:
            k = (l + r) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / k)

            if time > h:
                l = k + 1

            else:
                min_speed = k
                r = k - 1

        return min_speed

