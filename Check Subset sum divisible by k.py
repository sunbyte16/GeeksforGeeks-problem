class Solution:
    def divisibleByK(self, arr, k):
        # code here
        dp = [False] * k

        for num in arr:
            rem = num % k
            new_dp = dp[:]

            # Subset containing only the current element
            new_dp[rem] = True

            # Extend all existing subsets
            for r in range(k):
                if dp[r]:
                    new_dp[(r + rem) % k] = True

            dp = new_dp

            if dp[0]:
                return True

        return False
