class Solution:
    def prefixSum2D(self, mat, queries):
        n = len(mat)
        m = len(mat[0]) if n > 0 else 0

        # build prefix sum matrix: pref[i][j] = sum of submatrix (0,0) to (i,j)
        pref = [[0] * m for _ in range(n)]
        for i in range(n):
            row_sum = 0
            for j in range(m):
                row_sum += mat[i][j]
                pref[i][j] = row_sum
                if i > 0:
                    pref[i][j] += pref[i - 1][j]

        ans = []
        for r1, c1, r2, c2 in queries:
            total = pref[r2][c2]
            top = pref[r1 - 1][c2] if r1 > 0 else 0
            left = pref[r2][c1 - 1] if c1 > 0 else 0
            overlap = pref[r1 - 1][c1 - 1] if r1 > 0 and c1 > 0 else 0
            ans.append(total - top - left + overlap)
        return ans
