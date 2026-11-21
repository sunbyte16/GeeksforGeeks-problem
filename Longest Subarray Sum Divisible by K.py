class Solution:
    def longestSubarrayDivK(self, arr, k):
        # code here
        first = {0: -1}
        prefix_sum = 0
        max_len = 0

        for i, num in enumerate(arr):
            prefix_sum += num
            rem = prefix_sum % k

            if rem in first:
                max_len = max(max_len, i - first[rem])
            else:
                first[rem] = i

        return max_len
