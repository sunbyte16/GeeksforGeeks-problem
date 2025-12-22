class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        if n == 0:
            return -1
        m = len(arr[0])

        row = 0
        col = m - 1
        ans = -1

        # Start from top-right and do staircase traversal
        while row < n and col >= 0:
            if arr[row][col] == 1:
                ans = row        # this row has more 1s than all previous rows
                col -= 1         # move left to check if there are more 1s
            else:
                row += 1         # move down if current is 0

        return ans
