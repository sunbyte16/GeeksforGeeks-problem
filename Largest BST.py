class Solution:
    def largestBst(self, root):
        self.ans = 0

        def dfs(node):
            if not node:
                return (True, 0, float('inf'), float('-inf'))

            left = dfs(node.left)
            right = dfs(node.right)

            # Check BST condition
            if left[0] and right[0] and left[3] < node.data < right[2]:
                size = left[1] + right[1] + 1
                self.ans = max(self.ans, size)

                # return: isBST, size, min, max
                return (True, size,
                        min(node.data, left[2]),
                        max(node.data, right[3]))
            else:
                return (False,
                        max(left[1], right[1]),
                        0, 0)

        dfs(root)
        return self.ans
