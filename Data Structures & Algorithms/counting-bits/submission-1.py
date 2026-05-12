class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            temp = 0
            while i:
                i &= i - 1
                temp += 1
            res.append(temp)

        return res
