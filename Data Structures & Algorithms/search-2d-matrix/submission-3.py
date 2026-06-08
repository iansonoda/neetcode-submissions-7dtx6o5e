class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break

        if not (top <= bot):
            return False

        row = (top + bot) // 2

        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            mid = l + ((r - l)) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

