class Solution:

    def getMarks(self, l, r, rank):
        """code here"""
        from itertools import accumulate
        from bisect import bisect_left
        # how many elements in each interval
        arr = list(accumulate(r0-l0+1 for l0, r0 in zip(l, r)))
        ans = []
        for r in rank:
            i = bisect_left(arr, r)
            d = 0
            if i > 0:
                d = arr[i-1]
            ans.append(l[i]+r-d-1)
        return ans
