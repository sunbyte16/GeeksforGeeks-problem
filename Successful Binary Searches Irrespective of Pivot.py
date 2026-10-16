class Solution:
    def countAlwaysFound(self, arr):
        # code here
        n = len(arr)
        maxs, mins = [0]*n, [0]*n

        left = float('-inf')
        right = float('inf')
        for i in range(n):
            left = max(left, arr[i])
            maxs[i] = left
            right = min(right, arr[n-1-i])
            mins[n-1-i] = right


        return sum(int(e == mins[i] == maxs[i]) for i, e in enumerate(arr))
