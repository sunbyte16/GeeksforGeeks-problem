class Solution:
    def longestSubseq(self, arr):
        # code here
        dp = {}
        ans = 1
        for e in arr:
            d = max(dp.get(e-1, 1), dp.get(e+1, 1))
            dp[e] = max(dp.get(e, 1), d+1)
            ans = max(ans, d)
        return ans
