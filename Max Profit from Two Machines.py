class Solution:
    def maxProfit(self, x, y, a, b):

        n = len(a)

        # Store difference with index
        tasks = []

        for i in range(n):
            tasks.append((abs(a[i] - b[i]), a[i], b[i]))

        # Sort by maximum difference descending
        tasks.sort(reverse=True)

        profit = 0

        for diff, pa, pb in tasks:

            # Prefer Machine A
            if (pa >= pb and x > 0) or y == 0:
                profit += pa
                x -= 1

            # Prefer Machine B
            else:
                profit += pb
                y -= 1

        return profit
