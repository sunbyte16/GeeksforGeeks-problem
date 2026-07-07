class Solution:
    def largestArea(self, n, m, k, arr):
        # code here
        rows = sorted([r for r, c in arr] + [0, n+1])
        cols = sorted([c for r, c in arr] + [0, m+1])

        rg = max([rows[i] - rows[i-1] - 1 for i in range(1, len(rows))])
        cg = max([cols[i] - cols[i-1] - 1 for i in range(1, len(cols))])
        
        return rg*cg
        
