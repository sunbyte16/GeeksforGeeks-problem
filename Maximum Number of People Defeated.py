class Solution:
    def maxPeopleDefeated(self, p):
        low, high = 0, 10000

        while low <= high:
            mid = (low + high) // 2
            total = mid * (mid + 1) * (2 * mid + 1) // 6

            if total <= p:
                low = mid + 1
            else:
                high = mid - 1

        return high
