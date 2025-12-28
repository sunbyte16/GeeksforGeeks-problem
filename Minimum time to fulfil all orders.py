class Solution:
    def minTime(self, ranks, n):
        # Helper function to check if we can cook n pratas in given time
        def canCook(time):
            total = 0
            for r in ranks:
                t = 0
                cnt = 0
                while t + r * (cnt + 1) <= time:
                    cnt += 1
                    t += r * cnt
                total += cnt
                if total >= n:
                    return True
            return False

        lo = 0
        hi = max(ranks) * n * (n + 1) // 2
        ans = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            if canCook(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans
