class Solution:
    def findClosestPair(self, arr1, arr2, x):
        n = len(arr1)
        m = len(arr2)
        
        i = 0
        j = m - 1
        
        min_diff = float('inf')
        result = [0, 0]
        
        while i < n and j >= 0:
            curr_sum = arr1[i] + arr2[j]
            curr_diff = abs(curr_sum - x)
            
            # Update best pair
            if curr_diff < min_diff:
                min_diff = curr_diff
                result = [arr1[i], arr2[j]]
            
            # Move pointers
            if curr_sum > x:
                j -= 1
            else:
                i += 1
        
        return result
