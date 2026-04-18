class Solution:
    def longestSubarray(self, arr, k):  
        prefix_map = {}   # stores first occurrence of prefix sum
        curr_sum = 0
        max_len = 0
        
        for i in range(len(arr)):
            curr_sum += arr[i]
            
            # Case 1: subarray from 0 to i
            if curr_sum == k:
                max_len = i + 1
            
            # Case 2: subarray exists
            if (curr_sum - k) in prefix_map:
                length = i - prefix_map[curr_sum - k]
                max_len = max(max_len, length)
            
            # Store only first occurrence
            if curr_sum not in prefix_map:
                prefix_map[curr_sum] = i
        
        return max_len
