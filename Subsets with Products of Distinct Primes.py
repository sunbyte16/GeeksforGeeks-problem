class Solution:
    def countSubsets(self, arr):
        # code here
        mod = 10**9 + 7

        freq = [0] * 31
        for x in arr:
            freq[x] += 1

        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        mask = [0] * 31

        for i in range(2, 31):
            x = i
            m = 0
            ok = True

            for j, p in enumerate(prime):
                cnt = 0
                while x % p == 0:
                    cnt += 1
                    x //= p

                if cnt > 1:
                    ok = False
                    break

                if cnt == 1:
                    m |= (1 << j)

            if ok:
                mask[i] = m

        dp = [0] * 1024
        dp[0] = 1

        for i in range(2, 31):
            if freq[i] == 0 or mask[i] == 0:
                continue

            nxt = dp[:]

            for m in range(1024):
                if (m & mask[i]) == 0:
                    nxt[m | mask[i]] = (nxt[m | mask[i]] + dp[m] * freq[i]) % mod

            dp = nxt

        ans = sum(dp[1:]) % mod

        ones = pow(2, freq[1], mod)

        return (ans * ones) % mod
