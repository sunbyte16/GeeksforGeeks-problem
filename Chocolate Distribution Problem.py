class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        
        if m > n:
            return -1
        
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Initialize minimum difference
        min_diff = float('inf')
        
        # Step 3: Sliding window
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff
