class Solution:
    def maxSubsetXOR(self, arr):
        # Maximum bit needed for arr[i] <= 10^6
        basis = [0] * 21

        # Build XOR basis
        for num in arr:
            x = num

            for bit in range(20, -1, -1):
                if not (x & (1 << bit)):
                    continue

                if basis[bit]:
                    x ^= basis[bit]
                else:
                    basis[bit] = x
                    break

        # Find maximum possible XOR
        ans = 0

        for bit in range(20, -1, -1):
            ans = max(ans, ans ^ basis[bit])

        return ans
