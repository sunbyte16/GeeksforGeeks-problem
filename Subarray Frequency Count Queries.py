class Solution:
    def freqInRange(self, arr, queries):
        # code here
        from collections import defaultdict
        from bisect import bisect_left, bisect_right
        
        m = defaultdict(list)
        for i, e in enumerate(arr):
            m[e].append(i)
        
        ans = []
        for l, r, x in queries:
            il = bisect_left(m[x], l)
            ir = bisect_right(m[x], r)
            ans.append(ir-il)
        return ans
