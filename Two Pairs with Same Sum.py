class Solution:
    def findPairs(self, arr):
        # code here
        n = len(arr)
        pairs = {}

        # Store all index pairs for each sum
        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]
                pairs.setdefault(s, []).append((i, j))

        # Find the lexicographically smallest valid quadruplet
        for i in range(n):
            for j in range(i + 1, n):
                s = arr[i] + arr[j]

                for c, d in pairs[s]:
                    if (c, d) > (i, j):
                        if i != c and i != d and j != c and j != d:
                            return [i, j, c, d]

        return [-1, -1, -1, -1]
