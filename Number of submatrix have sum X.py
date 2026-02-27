class Solution:
    def countSquare(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        # Build prefix sum matrix
        prefix = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                prefix[i][j] = (
                    mat[i-1][j-1]
                    + prefix[i-1][j]
                    + prefix[i][j-1]
                    - prefix[i-1][j-1]
                )
        
        count = 0
        
        # Check all square sizes
        for size in range(1, min(n, m) + 1):
            for i in range(n - size + 1):
                for j in range(m - size + 1):
                    
                    total = (
                        prefix[i+size][j+size]
                        - prefix[i][j+size]
                        - prefix[i+size][j]
                        + prefix[i][j]
                    )
                    
                    if total == x:
                        count += 1
        
        return count
