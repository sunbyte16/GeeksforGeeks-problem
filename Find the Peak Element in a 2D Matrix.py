class Solution:
    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])

        low, high = 0, m - 1

        # Binary search on columns
        while low <= high:
            mid = (low + high) // 2

            # Find row index of max element in column mid
            max_row = 0
            for i in range(1, n):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i

            curr = mat[max_row][mid]
            left = mat[max_row][mid - 1] if mid - 1 >= 0 else float('-inf')
            right = mat[max_row][mid + 1] if mid + 1 < m else float('-inf')

            # If current is >= both left and right, check up/down and return if peak
            up = mat[max_row - 1][mid] if max_row - 1 >= 0 else float('-inf')
            down = mat[max_row + 1][mid] if max_row + 1 < n else float('-inf')

            if curr >= left and curr >= right and curr >= up and curr >= down:
                return [max_row, mid]

            # Move towards side with bigger neighbor (left/right)
            if right > curr:
                low = mid + 1
            else:
                high = mid - 1

        # Fallback (should not reach here if constraints guarantee a peak)
        return [-1, -1]
