from typing import List

class Solution:
    def cntSubsets(self, arr: List[int], l: int, r: int) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        freq = [0] * (n + 1)
        for x in arr:
            if x <= n:
                freq[x] += 1

        # exact MEX counts
        ans = 0
        ways = 1

        for mex in range(r + 1):
            if mex > 0:
                if freq[mex - 1] == 0:
                    break
                ways = ways * (pow(2, freq[mex - 1], MOD) - 1) % MOD

            if mex >= l:
                remaining = n - sum(freq[:mex + 1])
                count = ways * pow(2, remaining, MOD) % MOD
                ans = (ans + count) % MOD

        return ans   
