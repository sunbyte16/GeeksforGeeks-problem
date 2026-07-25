class Solution:
    def maximumSum(self, mat, k):
        # code here
        m, n = len(mat), len(mat[0])
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                prefix_sum[i][j] = (
                    mat[i][j]
                    + prefix_sum[i + 1][j]
                    + prefix_sum[i][j + 1]
                    - prefix_sum[i + 1][j + 1]
                )
        return max(
            prefix_sum[i][j]
            - prefix_sum[i + k][j]
            - prefix_sum[i][j + k]
            + prefix_sum[i + k][j + k]
            for i in range(m - k + 1) for j in range(n - k + 1)
        )
