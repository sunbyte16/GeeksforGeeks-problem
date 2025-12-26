class Solution:
    def kthMissing(self, arr, k):
        n = len(arr)
        
        # Binary search on index to find first index
        # where missing_count >= k
        lo, hi = 0, n  # hi can be n (virtual index after last element)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # Missing numbers up to arr[mid] (for mid < n):
            # arr[mid] should have been mid+1 if nothing missing,
            # so missing_count = arr[mid] - (mid+1)
            if mid < n and arr[mid] - (mid + 1) < k:
                lo = mid + 1
            else:
                hi = mid
        
        # Answer is lo + k
        return lo + k
