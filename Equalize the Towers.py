class Solution:
    def minCost(self, heights, cost):
        n = len(heights)

        def totalCost(h):
            total = 0
            for i in range(n):
                total += abs(heights[i] - h) * cost[i]
            return total

        left = min(heights)
        right = max(heights)
        ans = float('inf')

        while left <= right:
            mid = (left + right) // 2

            cost_mid = totalCost(mid)
            cost_mid_plus = totalCost(mid + 1)

            ans = min(ans, cost_mid)

            # Move towards lower cost
            if cost_mid_plus > cost_mid:
                right = mid - 1
            else:
                left = mid + 1

        return ans
