class Solution:
    def checkPath(self, adj: list[list[int]], u: int, v: int) -> bool:
        # code here
        visited = [False] * len(adj)
        stack = [u]
        visited[u] = True

        while stack:
            node = stack.pop()

            if node == v:
                return True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

        return False
