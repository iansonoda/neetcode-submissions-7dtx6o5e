class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        numPrereqs = [0] * numCourses
        adj = defaultdict(set)

        for src, dst in prerequisites:
            numPrereqs[dst] += 1
            adj[src].add(dst)

        q = deque()

        for n in range(numCourses):
            if numPrereqs[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                numPrereqs[nei] -= 1
                if numPrereqs[nei] == 0:
                    q.append(nei)

        return finish == numCourses

        