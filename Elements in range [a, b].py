class Solution:
    def cntInRange(self, arr, queries):
        import bisect
        
        # Sort the array once
        arr.sort()
        res = []
        
        for a, b in queries:
            # first index with value >= a
            left = bisect.bisect_left(arr, a)
            # first index with value > b
            right = bisect.bisect_right(arr, b)
            # count of elements in [a, b]
            res.append(right - left)
        
        return res
