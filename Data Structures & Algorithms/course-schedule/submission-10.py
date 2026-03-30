class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(set)
        degree = [0] * numCourses
        count = 0
        
        for a, b in prerequisites:
            adj[a].add(b)
            degree[b] += 1

        q = deque()
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            count += 1
            for pre in adj[course]:
                degree[pre] -= 1
                if degree[pre] == 0:
                    q.append(pre)
        return count == numCourses