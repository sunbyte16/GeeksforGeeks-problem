class Solution:
    def maxProduct(self, arr):
        max_ending = arr[0]
        min_ending = arr[0]
        ans = arr[0]

        for i in range(1, len(arr)):
            x = arr[i]

            if x < 0:
                max_ending, min_ending = min_ending, max_ending

            max_ending = max(x, max_ending * x)
            min_ending = min(x, min_ending * x)

            ans = max(ans, max_ending)

        return ans
