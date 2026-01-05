class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        
        # Initial window sum
        window_sum = sum(arr[:k])
        max_sum = window_sum
        
        # Slide the window
        for i in range(k, n):
            window_sum += arr[i]      # add next element
            window_sum -= arr[i - k]  # remove leftmost element
            max_sum = max(max_sum, window_sum)
        
        return max_sum
