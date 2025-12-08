class Solution:
    def matrixChainOrder(self, arr):
        n = len(arr)
        m = n - 1  # number of matrices
        if m == 1:
            return "A"

        # dp[i][j]: min cost to multiply matrices i..j (1-based)
        INF = 10**18
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        split = [[0] * (m + 1) for _ in range(m + 1)]

        # chain length
        for length in range(2, m + 1):
            for i in range(1, m - length + 2):
                j = i + length - 1
                dp[i][j] = INF
                for k in range(i, j):
                    cost = (dp[i][k] +
                            dp[k + 1][j] +
                            arr[i - 1] * arr[k] * arr[j])
                    if cost < dp[i][j]:
                        dp[i][j] = cost
                        split[i][j] = k

        # build result string
        def build(i, j):
            if i == j:
                return chr(ord('A') + i - 1)
            k = split[i][j]
            left = build(i, k)
            right = build(k + 1, j)
            return "(" + left + right + ")"

        return build(1, m)
