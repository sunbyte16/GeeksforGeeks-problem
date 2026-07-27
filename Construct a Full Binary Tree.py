''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def constructBinaryTree(self, pre, preMirror):
        # code here
        i, j = 0, len(pre) - 1

        def build() -> Node:
            nonlocal i, j
            node = Node(pre[i])
            if pre[i] == preMirror[j]:
                i += 1
                j -= 1
            else:
                i += 1
                node.left = build()
                node.right = build()
                j -= 1
            return node

        return build()
