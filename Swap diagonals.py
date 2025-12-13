class Solution:
    def swapDiagonal(self, mat):
        n = len(mat)
        for i in range(n):
            j = n - 1 - i
            # swap major (i,i) with minor (i,j)
            mat[i][i], mat[i][j] = mat[i][j], mat[i][i]
        return mat
