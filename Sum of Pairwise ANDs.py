class Solution:
    def pairAndSum(self, Arr):
        ans = 0

        # Arr[i] <= 10^8, so 28 bits are sufficient
        for bit in range(28):
            mask = 1 << bit
            cnt = 0

            for x in Arr:
                if x & mask:
                    cnt += 1

            # Number of pairs where this bit is set in both elements
            ans += (cnt * (cnt - 1) // 2) * mask

        return ans
