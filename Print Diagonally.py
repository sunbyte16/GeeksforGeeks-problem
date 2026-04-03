class Solution:
    def diagView(self, mat):
        n = len(mat)
        result = []
        
        # total diagonals = 2*n - 1
        for s in range(2 * n - 1):
            
            if s < n:
                row = 0
                col = s
            else:
                row = s - n + 1
                col = n - 1
            
            # traverse current diagonal
            while row < n and col >= 0:
                result.append(mat[row][col])
                row += 1
                col -= 1
        
        return result
