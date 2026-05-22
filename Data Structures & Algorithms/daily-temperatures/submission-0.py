class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popped = stack.pop()
                res[popped[1]] = i - popped[1]

            stack.append((temp, i))

        while stack:
            popped = stack.pop()
            res[popped[1]] = 0

        return res