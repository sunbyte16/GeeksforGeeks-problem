class Solution:
    def maxProduct(self, arr, k):
        dp_min = [None] * (k + 1)
        dp_max = [None] * (k + 1)

        dp_min[0] = dp_max[0] = 1

        for x in arr:
            for j in range(k, 0, -1):
                if dp_min[j - 1] is not None:
                    a = dp_min[j - 1] * x
                    b = dp_max[j - 1] * x

                    mn = min(a, b)
                    mx = max(a, b)

                    if dp_min[j] is None:
                        dp_min[j] = mn
                        dp_max[j] = mx
                    else:
                        dp_min[j] = min(dp_min[j], mn)
                        dp_max[j] = max(dp_max[j], mx)

        return dp_max[k]
