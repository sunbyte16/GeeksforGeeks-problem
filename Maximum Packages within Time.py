class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        n = len(arr)

        window_sum = sum(arr[:totalTime])
        ans = window_sum

        for i in range(totalTime, n):
            window_sum += arr[i] - arr[i - totalTime]
            ans = max(ans, window_sum)

        return ans
