class Solution:
    def prefixStrings(self, n: int) -> int:
        # code here
        MOD = 10**9 + 7

        # factorials up to 2n
        fact = [1] * (2 * n + 1)
        for i in range(1, 2 * n + 1):
            fact[i] = fact[i - 1] * i % MOD

        # nCr = fact[2n] / (fact[n] * fact[n])
        # Fermat's little theorem: a^(-1) = a^(MOD-2) mod MOD
        inv_fact_n = pow(fact[n], MOD - 2, MOD)

        comb = fact[2 * n] * inv_fact_n % MOD
        comb = comb * inv_fact_n % MOD

        # Catalan number = C(2n, n) / (n + 1)
        ans = comb * pow(n + 1, MOD - 2, MOD) % MOD

        return ans
