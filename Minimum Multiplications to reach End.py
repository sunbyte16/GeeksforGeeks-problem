from collections import deque

class Solution:
    def minSteps(self, arr, start, end):

        if start == end:
            return 0

        q = deque()
        q.append((start, 0))

        vis = [False] * 1000
        vis[start] = True

        while q:

            num, steps = q.popleft()

            for x in arr:

                nxt = (num * x) % 1000

                if nxt == end:
                    return steps + 1

                if not vis[nxt]:

                    vis[nxt] = True
                    q.append((nxt, steps + 1))

        return -1
