import heapq

class Solution:
    def maxAmount(self, arr, k):
        q = [-x for x in arr]
        heapq.heapify(q)

        res = 0
        mod = 10**9 + 7

        while k > 0:
            n = -heapq.heappop(q)
            res += n
            heapq.heappush(q, -max(0, n - 1))
            k -= 1

        return res % mod
