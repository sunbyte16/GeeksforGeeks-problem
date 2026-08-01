class Solution:
    def findMax(self, n, a, b, k):
        # code here
        diffs = [0] * (n + 1)
        for l, r, w in zip(a, b, k):
            diffs[l] += w
            diffs[r + 1] -= w
        curr = maxi = 0
        for d in diffs:
            curr += d
            if curr >= maxi:
                maxi = curr
        return maxi
