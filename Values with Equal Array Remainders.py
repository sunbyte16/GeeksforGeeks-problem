class Solution:
    def sameMod(self, arr):
        import math

        g = 0

        for i in range(1, len(arr)):
            g = math.gcd(g, abs(arr[i] - arr[0]))

        if g == 0:
            return -1

        count = 0
        i = 1

        while i * i <= g:
            if g % i == 0:
                count += 1
                if i != g // i:
                    count += 1
            i += 1

        return count
