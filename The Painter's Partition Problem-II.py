class Solution:
    def minTime(self, arr, k):
        n = len(arr)

        # If painters >= boards, answer is max board
        if k >= n:
            return max(arr)

        low = max(arr)
        high = sum(arr)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if self.isPossible(arr, k, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def isPossible(self, arr, k, maxTime):
        painters = 1
        curr = 0

        for board in arr:
            if curr + board <= maxTime:
                curr += board
            else:
                painters += 1
                curr = board
                if painters > k:
                    return False

        return True
