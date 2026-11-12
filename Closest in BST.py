class Solution:
    def minDiff(self, root, k):
        ans = float('inf')
        curr = root

        while curr:
            ans = min(ans, abs(curr.data - k))

            if ans == 0:
                return 0

            if k < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        return ans
