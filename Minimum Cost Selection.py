class Solution:

    def minCost(self, mat):
        """code here"""
        dp = mat[0][:]

        # Process remaining rows
        for i in range(1, len(mat)):
            a, b, c = dp
            dp = [
                mat[i][0] + min(b, c),
                mat[i][1] + min(a, c),
                mat[i][2] + min(a, b)
            ]

        return min(dp)
