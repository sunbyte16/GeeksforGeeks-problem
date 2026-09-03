class Solution:

    def maxFruits(self, arr: list[int], m: int) -> int:
        """ code here """
        n = len(arr)
        maxi = curr = sum(arr[:m])
        for i in range(m, n):
            curr += arr[i] - arr[i - m]
            if curr > maxi:
                maxi = curr
        for i in range(m - 1):
            curr += arr[i] - arr[-m + i]
            if curr > maxi:
                maxi = curr
        return maxi
