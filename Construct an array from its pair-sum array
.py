class Solution:
    def constructArr(self, arr):
        import math
        
        m = len(arr)
        
        # if only one pair-sum, original array has size 2
        if m == 1:
            return [1, arr[0] - 1]
        
        # find n from m = n*(n-1)/2  => n^2 - n - 2m = 0
        # n = (1 + sqrt(1 + 8m)) / 2
        n = int((1 + math.isqrt(1 + 8 * m)) // 2)
        
        res = [0] * n
        
        # deduce res[0] using first three relevant pair-sums
        res[0] = (arr[0] + arr[1] - arr[n - 1]) // 2
        
        # deduce the remaining elements
        for i in range(1, n):
            res[i] = arr[i - 1] - res[0]
        
        return res