''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        # code here
        MIN_VALUE = -10 ** 5

        def dfs(node: "Optional[Node]", max_ancestor: int) -> int:
            if node is None:
                return MIN_VALUE
            new_max_ancestor = max(max_ancestor, node.data)
            return max(
                max_ancestor - node.data,
                dfs(node.left, new_max_ancestor),
                dfs(node.right, new_max_ancestor)
            )

        return dfs(root, MIN_VALUE)
