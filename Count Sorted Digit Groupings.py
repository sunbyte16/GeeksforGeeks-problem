class Solution:
    
    def validGroups(self, s):

        n = len(s)

        dp = {}

        # Recursive function
        def solve(index, prev_sum):

            # If end reached
            if index == n:
                return 1

            # Memoization
            if (index, prev_sum) in dp:
                return dp[(index, prev_sum)]

            ways = 0
            current_sum = 0

            # Try all partitions
            for j in range(index, n):

                current_sum += int(s[j])

                # Non-decreasing condition
                if current_sum >= prev_sum:
                    ways += solve(j + 1, current_sum)

            dp[(index, prev_sum)] = ways

            return ways

        return solve(0, 0)
