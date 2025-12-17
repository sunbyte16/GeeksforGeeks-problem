class Solution:
    def mergeOverlap(self, arr):
        if not arr:
            return []

        # Sort intervals by start time
        arr.sort(key=lambda x: x[0])

        res = [arr[0]]
        for s, e in arr[1:]:
            last_s, last_e = res[-1]
            if s <= last_e:  # overlap
                res[-1][1] = max(last_e, e)
            else:
                res.append([s, e])

        return res
