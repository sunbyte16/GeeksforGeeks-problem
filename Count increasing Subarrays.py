class Solution:
    def countIncreasing(self, arr):
        n = len(arr)
        if n < 2:
            return 0
        
        count = 0
        length = 1  # current increasing streak length
        
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                length += 1
            else:
                # add subarrays from previous streak
                if length >= 2:
                    count += (length * (length - 1)) // 2
                length = 1
        
        # handle last streak
        if length >= 2:
            count += (length * (length - 1)) // 2
        
        return count
