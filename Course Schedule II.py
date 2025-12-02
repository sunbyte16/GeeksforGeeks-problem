class Solution:
    def findOrder(self, n, prerequisites):
        from collections import deque, defaultdict
        
        # Build graph and compute in-degrees
        graph = defaultdict(list)
        in_degree = [0] * n
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        # Initialize queue with courses having no prerequisites
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        order = []
        
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If order includes all courses, return it; otherwise, return []
        return order if len(order) == n else []
