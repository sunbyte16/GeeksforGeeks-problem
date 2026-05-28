from collections import defaultdict, deque

class Solution:
    
    def verticalSum(self, root):

        if not root:
            return []

        q = deque([(root, 0)])

        d = defaultdict(int)

        while q:

            node, dis = q.popleft()

            d[dis] += node.data

            if node.left:
                q.append((node.left, dis - 1))

            if node.right:
                q.append((node.right, dis + 1))

        ans = []

        for key in sorted(d.keys()):
            ans.append(d[key])

        return ans
