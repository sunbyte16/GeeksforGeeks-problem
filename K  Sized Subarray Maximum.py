from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        dq = deque()
        result = []

        for i in range(n):
            # Remove indices that are out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove elements smaller than current from the back
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            # Add maximum for current window
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
