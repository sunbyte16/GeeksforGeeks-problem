class Solution:
    def maxPathSum(self, a, b):
        # Code here
        sum_a = sum_b = max_sum = 0
        m, n = len(a), len(b)
        i = j = 0
        while i < m and j < n:
            if a[i] < b[j]:
                sum_a += a[i]
                i += 1
            elif a[i] == b[j]:
                max_sum += max(sum_a, sum_b) + a[i]
                i += 1
                j += 1
                sum_a = sum_b = 0
            else:
                sum_b += b[j]
                j += 1
        sum_a += sum(a[i:])
        sum_b += sum(b[j:])
        max_sum += max(sum_a, sum_b)
        return max_sum
