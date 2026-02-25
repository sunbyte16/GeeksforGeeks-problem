class Solution:
    def longestSubarray(self, arr, k):
        prefix_map = {}
        prefix_sum = 0
        max_len = 0
        
        for i in range(len(arr)):
            # Transform
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            
            # Case 1: whole subarray from 0 to i
            if prefix_sum > 0:
                max_len = i + 1
            
            # Store first occurrence
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
            
            # Case 2: find prefix_sum - 1
            if (prefix_sum - 1) in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum - 1])
        
        return max_len
