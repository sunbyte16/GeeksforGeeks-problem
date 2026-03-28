class Solution:
    def articulationPoints(self, V, edges):
        # Step 1: Build adjacency list
        graph = [[] for _ in range(V)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Initialize arrays
        visited = [False] * V
        tin = [-1] * V
        low = [-1] * V
        isArticulation = [False] * V

        timer = 0

        # Step 3: DFS function
        def dfs(u, parent):
            nonlocal timer
            visited[u] = True
            tin[u] = low[u] = timer
            timer += 1

            children = 0

            for v in graph[u]:
                if v == parent:
                    continue

                if not visited[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                    # Condition for articulation point
                    if low[v] >= tin[u] and parent != -1:
                        isArticulation[u] = True

                    children += 1
                else:
                    low[u] = min(low[u], tin[v])

            # Root node case
            if parent == -1 and children > 1:
                isArticulation[u] = True

        # Step 4: Handle disconnected graph
        for i in range(V):
            if not visited[i]:
                dfs(i, -1)

        # Step 5: Collect result
        result = [i for i in range(V) if isArticulation[i]]

        return result if result else [-1]
