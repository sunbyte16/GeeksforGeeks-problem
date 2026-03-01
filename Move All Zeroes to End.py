class Solution:
    def pushZerosToEnd(self, arr):
        n = len(arr)
        pos = 0  # Position to place next non-zero element
        
        # Move non-zero elements forward
        for i in range(n):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
        
        # Fill remaining positions with 0
        while pos < n:
            arr[pos] = 0
            pos += 1
        
        return arr
