from collections import deque

class Solution:
    def minTime(self, root, target):
        
        # Step 1: Create parent map + find target node
        parent = {}
        target_node = None
        
        def build(node, par):
            nonlocal target_node
            if not node:
                return
            
            if node.data == target:
                target_node = node
            
            parent[node] = par
            
            build(node.left, node)
            build(node.right, node)
        
        build(root, None)
        
        # Step 2: BFS to burn tree
        q = deque()
        q.append(target_node)
        
        visited = set()
        visited.add(target_node)
        
        time = -1
        
        while q:
            size = len(q)
            time += 1
            
            for _ in range(size):
                node = q.popleft()
                
                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        
        return time
