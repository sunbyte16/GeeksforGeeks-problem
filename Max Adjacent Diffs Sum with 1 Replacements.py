class Solution:
    def maxDiffSum(self, arr):
        # code here
        n = len(arr)

        if n <= 1:
            return 0

        # dp0 = maximum sum till previous index
        #       when previous element is replaced by 1
        # dp1 = maximum sum till previous index
        #       when previous element remains arr[i]
        dp0 = 0
        dp1 = 0

        for i in range(1, n):
            new_dp0 = max(
                dp0 + abs(1 - 1),
                dp1 + abs(arr[i - 1] - 1)
            )

            new_dp1 = max(
                dp0 + abs(1 - arr[i]),
                dp1 + abs(arr[i - 1] - arr[i])
            )

            dp0 = new_dp0
            dp1 = new_dp1

        return max(dp0, dp1)
