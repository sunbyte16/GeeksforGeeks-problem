class Solution:
	def shortestDist(self, mat):
		# code here
		n = len(mat)

        if n == 1:
            return [[1]]

        ans = [[0] * n for _ in range(n)]
        bad = [[False] * n for _ in range(n)]

        def dfs(i, j):
            if i == n - 1 and j == n - 1:
                ans[i][j] = 1
                return True

            if bad[i][j]:
                return False

            if mat[i][j] == 0:
                return False

            ans[i][j] = 1

            # smaller jumps first
            for jump in range(1, mat[i][j] + 1):

                # right first
                nj = j + jump
                if nj < n and ans[i][nj] == 0:
                    if dfs(i, nj):
                        return True

                # then down
                ni = i + jump
                if ni < n and ans[ni][j] == 0:
                    if dfs(ni, j):
                        return True

            ans[i][j] = 0
            bad[i][j] = True
            return False

        if dfs(0, 0):
            return ans

        return [[-1]]
