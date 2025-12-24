class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        if n == 0:
            return 0

        # Helper: find index of smallest element (pivot) in rotated sorted array
        def find_pivot(a):
            l, r = 0, n - 1
            while l < r:
                mid = (l + r) // 2
                if a[mid] > a[r]:
                    l = mid + 1
                else:
                    r = mid
            return l  # index of minimum element

        # Helper: count elements <= x in a sorted subarray a[l..r]
        def count_in_sorted(a, l, r, x):
            if l > r:
                return 0
            # first index > x in [l, r]
            import bisect
            idx = bisect.bisect_right(a, x, l, r + 1)
            return max(0, idx - l)

        pivot = find_pivot(arr)

        # If array is not rotated or x is >= last element, all <= x are in [0..??] straightforwardly
        # But generic logic: handle two sorted parts [0..pivot-1] and [pivot..n-1]
        cnt1 = count_in_sorted(arr, 0, pivot - 1, x)
        cnt2 = count_in_sorted(arr, pivot, n - 1, x)

        return cnt1 + cnt2
