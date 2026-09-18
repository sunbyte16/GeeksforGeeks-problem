class Solution:
    def absDiff(self, root):
        stack = []
        cur = root
        prev = None
        ans = float('inf')

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()

            if prev is not None:
                ans = min(ans, cur.data - prev)

            prev = cur.data
            cur = cur.right

        return ans
