class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visited = set()
        order = []

        def dfs(course):
            if course in visited:
                return False

            if preMap[course] == []:
                if course not in order:
                    order.append(course)
                return True

            visited.add(course)

            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            preMap[course] = []

            if course not in order:
                order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order