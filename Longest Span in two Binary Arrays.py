class Solution:
    def equalSumSpan(self, a1, a2):
        n = len(a1)
        
        # Dictionary to store first occurrence of prefix sum
        prefix_map = {}
        
        max_len = 0
        prefix_sum = 0
        
        for i in range(n):
            # Compute difference and update prefix sum
            prefix_sum += (a1[i] - a2[i])
            
            # If prefix sum is 0 → span from 0 to i
            if prefix_sum == 0:
                max_len = i + 1
            
            # If seen before → subarray sum is 0
            if prefix_sum in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum])
            else:
                # Store first occurrence only
                prefix_map[prefix_sum] = i
        
        return max_len
