'''
Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def longestConsecutive(self, root):
        # Code here
        def dfs(node, prev_val, prev_len):
            if node is None:
                return prev_len
            curr_len = prev_len + 1 if node.data == prev_val + 1 else 1
            return max(
                curr_len,
                dfs(node.left, node.data, curr_len),
                dfs(node.right, node.data, curr_len)
            )

        max_len = dfs(root, -1, -1)
        return max_len if max_len > 1 else -1
