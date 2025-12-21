class Solution:
    def countXInRange(self, arr, queries):
        import bisect
        
        result = []
        n = len(arr)
        
        for l, r, x in queries:
            # Find first occurrence >= x in arr[l:r+1]
            left = bisect.bisect_left(arr, x, l, r + 1)
            
            # Find first occurrence > x in arr[l:r+1] 
            right = bisect.bisect_right(arr, x, l, r + 1)
            
            # Count of x is right - left
            result.append(right - left)
        
        return result
