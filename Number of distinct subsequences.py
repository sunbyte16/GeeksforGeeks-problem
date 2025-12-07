class Solution:
    def distinctSubseq(self, s):
        MOD = 10**9 + 7
        last = [0] * 26   # last contribution per character
        res = 1           # start with empty subsequence

        for ch in s:
            idx = ord(ch) - ord('a')
            new_res = (2 * res % MOD - last[idx] + MOD) % MOD
            last[idx] = res
            res = new_res

        return res % MOD
