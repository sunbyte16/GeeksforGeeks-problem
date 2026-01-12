from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        dq = deque()
        result = []

        for i in range(n):
            # Remove indices out of current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements from the back
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            # Append max once first window is complete
            if i >= k - 1:
                result.append(arr[dq[0]])

        return result
