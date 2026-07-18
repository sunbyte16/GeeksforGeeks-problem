class Solution:
    def processQueries(self, arr, queries):
        n = len(arr)

        # inc[i] = farthest index reachable while non-decreasing
        inc = [0] * n
        inc[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] <= arr[i + 1]:
                inc[i] = inc[i + 1]
            else:
                inc[i] = i

        # dec[i] = farthest index reachable while non-increasing
        dec = [0] * n
        dec[n - 1] = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                dec[i] = dec[i + 1]
            else:
                dec[i] = i

        ans = []
        for l, r in queries:
            peak = inc[l]
            ans.append(dec[peak] >= r)

        return ans
