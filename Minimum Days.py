class Solution:
    def getMinimumDays(self, s, p):
        n = len(s)

        # Check whether the original string is valid
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                break
        else:
            return 0

        # Store replacement day for each index
        day = [0] * n

        for i in range(n):
            day[p[i]] = i + 1

        ans = 0

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                ans = max(ans, min(day[i], day[i + 1]))

        return ans
