class Solution:
    def maxValue(self, n: int) -> int:
        ans = 0
        run = 0  # consecutive set bits so far

        for i in range(n.bit_length() - 1, -1, -1):
            bit = (n >> i) & 1
            ans <<= 1

            if bit and run == 2:
                bit = 0
                run = 0
            else:
                run = run + 1 if bit else 0

            ans |= bit

        return ans
