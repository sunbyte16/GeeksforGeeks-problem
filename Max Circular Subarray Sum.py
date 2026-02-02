class Solution:
    def maxCircularSum(self, arr):
        total_sum = 0
        
        max_ending = min_ending = 0
        max_kadane = float('-inf')
        min_kadane = float('inf')
        
        for x in arr:
            total_sum += x
            
            # Kadane for max
            max_ending = max(x, max_ending + x)
            max_kadane = max(max_kadane, max_ending)
            
            # Kadane for min
            min_ending = min(x, min_ending + x)
            min_kadane = min(min_kadane, min_ending)
        
        # If all numbers are negative
        if max_kadane < 0:
            return max_kadane
        
        # Circular case
        max_wrap = total_sum - min_kadane
        
        return max(max_kadane, max_wrap)
