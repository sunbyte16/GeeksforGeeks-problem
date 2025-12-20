class Solution:
    def searchInsertK(self, arr, k):
        n = len(arr)
        lo, hi = 0, n - 1
        ans = n  # default: insert at end
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] >= k:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans
