class Solution:
    def largestSquare(self, mat: list[list[int]], queries: list[list[int]], k: int) -> list[int]:
        # code here
        n = len(mat)
        m = len(mat[0])
        
        # 1. Build 2D Prefix Sum Matrix
        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                pref[i + 1][j + 1] = mat[i][j] + pref[i][j + 1] + pref[i + 1][j] - pref[i][j]
                
        def get_sum(r1, c1, r2, c2):
            return pref[r2 + 1][c2 + 1] - pref[r1][c2 + 1] - pref[r2 + 1][c1] + pref[r1][c1]
        
        ans = []
        
        # 2. Process each query using Binary Search
        for r, c in queries:
            # Check if even the center cell itself violates the limit 'k'
            if mat[r][c] > k:
                ans.append(-1)
                continue
            
            # Maximum allowed radius such that square stays within matrix boundaries
            max_d = min(r, n - 1 - r, c, m - 1 - c)
            
            low, high = 0, max_d
            best_d = 0
            
            while low <= high:
                mid = (low + high) // 2
                
                # Check sum of 1s in square centered at (r, c) with radius `mid`
                ones_count = get_sum(r - mid, c - mid, r + mid, c + mid)
                
                if ones_count <= k:
                    best_d = mid
                    low = mid + 1  # Try expanding further
                else:
                    high = mid - 1 # Reduce square size
            
            # Side length = 2 * radius + 1
            ans.append(2 * best_d + 1)
            
        return ans
