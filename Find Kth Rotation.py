class Solution:
    def findKRotation(self, arr):
        low = 0
        high = len(arr) - 1
        n = len(arr)

        while low <= high:
            # If array is already sorted
            if arr[low] <= arr[high]:
                return low

            mid = (low + high) // 2
            next = (mid + 1) % n
            prev = (mid - 1 + n) % n

            # Check if mid is minimum
            if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
                return mid

            # Left part sorted → go right
            if arr[low] <= arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return 0
