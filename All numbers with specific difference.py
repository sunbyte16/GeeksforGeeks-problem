class Solution:
    def getCount(self, n, d):
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
        # Numbers >= d+90 are always valid
        if n < d:
            return 0
        
        guaranteed = max(0, n - (d + 90) + 1)
        
        count = 0
        for x in range(d, min(n + 1, d + 90)):
            if x - digit_sum(x) >= d:
                count += 1
        
        return guaranteed + count
