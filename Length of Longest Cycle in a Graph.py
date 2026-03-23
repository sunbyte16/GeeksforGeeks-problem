class Solution:
    def longestCycle(self, V, edges):
        # convert to adjacency (since max 1 outgoing)
        graph = [-1] * V
        for u, v in edges:
            graph[u] = v

        visited = [False] * V
        ans = -1

        for i in range(V):
            if visited[i]:
                continue

            curr = i
            timeVisited = {}
            step = 0

            while curr != -1 and not visited[curr]:
                visited[curr] = True
                timeVisited[curr] = step
                step += 1
                curr = graph[curr]

                if curr in timeVisited:
                    cycle_len = step - timeVisited[curr]
                    ans = max(ans, cycle_len)
                    break

        return ans
