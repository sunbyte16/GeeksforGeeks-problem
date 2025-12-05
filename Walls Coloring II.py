from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0]) if costs[0] else 0
        if k == 0:
            return -1
        if k == 1 and n > 1:
            return -1

        # prevMin1, prevMin2: smallest and second smallest costs of previous row
        # minIdx: color index of prevMin1
        prevMin1 = float('inf')
        prevMin2 = float('inf')
        minIdx = -1

        # Initialize for first wall
        for j in range(k):
            val = costs[0][j]
            if val < prevMin1:
                prevMin2 = prevMin1
                prevMin1 = val
                minIdx = j
            elif val < prevMin2:
                prevMin2 = val

        # Process remaining walls
        for i in range(1, n):
            curMin1 = float('inf')
            curMin2 = float('inf')
            curIdx = -1

            for j in range(k):
                # If we choose color j for this wall:
                if j == minIdx:
                    cost = costs[i][j] + prevMin2
                else:
                    cost = costs[i][j] + prevMin1

                # Update current min1, min2
                if cost < curMin1:
                    curMin2 = curMin1
                    curMin1 = cost
                    curIdx = j
                elif cost < curMin2:
                    curMin2 = cost

            prevMin1, prevMin2, minIdx = curMin1, curMin2, curIdx

        return prevMin1 if prevMin1 != float('inf') else -1
