class Solution:
    def largestSubsquare(self, mat):
        n = len(mat)

        left = [[0] * n for _ in range(n)]
        top = [[0] * n for _ in range(n)]

        ans = 0

        for i in range(n):
            for j in range(n):
                if mat[i][j] == 'X':
                    left[i][j] = 1 + (left[i][j - 1] if j else 0)
                    top[i][j] = 1 + (top[i - 1][j] if i else 0)

        for i in range(n):
            for j in range(n):
                size = min(left[i][j], top[i][j])

                while size > ans:
                    r = i - size + 1
                    c = j - size + 1

                    if left[r][j] >= size and top[i][c] >= size:
                        ans = size
                        break

                    size -= 1

        return ans
