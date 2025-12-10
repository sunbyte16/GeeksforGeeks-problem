class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        
        # expected sums
        S = n * (n + 1) // 2
        S2 = n * (n + 1) * (2 * n + 1) // 6
        
        # actual sums from array
        sumArr = 0
        sumSqArr = 0
        for v in arr:
            sumArr += v
            sumSqArr += v * v
        
        diff = sumArr - S          # x - y
        diffSq = sumSqArr - S2     # x^2 - y^2 = (x - y)(x + y)
        
        sum_xy = diffSq // diff    # x + y
        
        x = (diff + sum_xy) // 2   # repeating
        y = x - diff               # missing
        
        return [x, y]
