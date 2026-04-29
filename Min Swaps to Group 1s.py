class Solution:
    def minSwaps(self, arr):
        ones = sum(arr)
        
        # No 1s case
        if ones == 0:
            return -1
        
        # Count 1s in first window
        curr = sum(arr[:ones])
        max_ones = curr
        
        # Sliding window
        for i in range(ones, len(arr)):
            curr += arr[i]        # add new
            curr -= arr[i-ones]  # remove old
            
            max_ones = max(max_ones, curr)
        
        return ones - max_ones
