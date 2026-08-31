class Solution:
    def minCost(self, n, i, d, c):
        INF = 10**30

        # Collect all states needed by repeatedly taking
        # floor(x/2) and ceil(x/2)
        states = {0, 1, n}
        stack = [n]

        while stack:
            x = stack.pop()

            if x <= 1:
                continue

            a = x // 2
            b = (x + 1) // 2

            if a not in states:
                states.add(a)
                stack.append(a)

            if b not in states:
                states.add(b)
                stack.append(b)

        states = sorted(states)

        dp = {0: 0}

        for x in states:
            if x == 0:
                continue

            # Always possible: insert x characters
            ans = x * i

            if x == 1:
                dp[x] = ans
                continue

            if x % 2 == 0:
                # x/2 -> double
                ans = min(ans, dp[x // 2] + c)
            else:
                # (x-1)/2 -> double -> insert
                ans = min(ans, dp[x // 2] + c + i)

                # (x+1)/2 -> double -> delete
                upper = (x + 1) // 2
                ans = min(ans, dp[upper] + c + d)

            dp[x] = ans

        return dp[n]
