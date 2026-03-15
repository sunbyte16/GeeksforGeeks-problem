from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root): 
        if not root:
            return []
        
        mp = defaultdict(list)
        q = deque()
        
        # (node, horizontal_distance)
        q.append((root, 0))
        
        while q:
            node, hd = q.popleft()
            
            mp[hd].append(node.data)
            
            if node.left:
                q.append((node.left, hd - 1))
            
            if node.right:
                q.append((node.right, hd + 1))
        
        result = []
        for key in sorted(mp.keys()):
            result.append(mp[key])
        
        return result
