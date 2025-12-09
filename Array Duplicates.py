class Solution:
    def findDuplicates(self, arr):
        n = len(arr)
        res = []
        
        for i in range(n):
            val = abs(arr[i])
            idx = val - 1
            if arr[idx] > 0:
                arr[idx] = -arr[idx]   # first time seen
            else:
                res.append(val)        # second time seen
        
        return res
