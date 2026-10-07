class Solution:
    def maxPathSum(self, root):
        ans = float('-inf')

        def dfs(n):
            nonlocal ans

            if not n:
                return float('-inf')

            if not n.left and not n.right:
                return n.data

            left = dfs(n.left)
            right = dfs(n.right)

            if n.left and n.right:
                ans = max(ans, left + n.data + right)

            return n.data + max(left, right)

        dfs(root)

        return -1 if ans == float('-inf') else ans
