class Solution:
    def maxOnes(self, arr):
        total_ones = 0
        max_gain = 0
        curr_gain = 0
        
        for num in arr:
            if num == 1:
                total_ones += 1
                val = -1
            else:
                val = 1
            
            curr_gain = max(val, curr_gain + val)
            max_gain = max(max_gain, curr_gain)
        
        return total_ones + max_gain
