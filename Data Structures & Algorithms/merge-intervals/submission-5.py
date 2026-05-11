class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        curInterval = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if curInterval[1] < intervals[i][0]:
                res.append(curInterval)
                curInterval = intervals[i]

            else:
                curInterval = [min(curInterval[0], intervals[i][0]), max(curInterval[1], intervals[i][1])]

        res.append(curInterval)

        return res
