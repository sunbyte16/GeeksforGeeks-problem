from collections import deque

class Solution:
    def getCount(self, root, k):
        q = deque([(root, 1)])
        costs = []

        while q:
            node, level = q.popleft()

            if node.left is None and node.right is None:
                costs.append(level)
                continue

            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

        costs.sort()

        count = 0
        for cost in costs:
            if cost > k:
                break
            k -= cost
            count += 1

        return count
