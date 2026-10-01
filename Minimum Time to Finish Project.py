from collections import deque

class Solution:
    def minTime(self, duration, dependencies):
        n = len(duration)

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v in dependencies:
            graph[u].append(v)
            indegree[v] += 1

        # Earliest time each module finishes
        finish = duration[:]

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        completed = 0

        while q:
            u = q.popleft()
            completed += 1

            for v in graph[u]:
                finish[v] = max(finish[v], finish[u] + duration[v])
                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        # Cycle exists
        if completed != n:
            return -1

        return max(finish)
