class Solution:
    def minTime(self, a: int, b: int, d: int, l: int, r: int) -> int
        # code here
        MOD = 10**9 + 7
        c = a - b

        # Minimum time using normal movement only
        q = (d - a + c - 1) // c
        normal_time = d + 2 * b * q

        # Minimum time using a jump of length j,
        # where T = d - j
        def jump_time(T):
            q = max(0, (T - a + c - 1) // c)
            return T + 1 + 2 * b * q

        # Sum of ceil(x / c) for x = 1 to m
        def prefix(m):
            if m <= 0:
                return 0

            q, rem = divmod(m, c)
            return m + c * q * (q - 1) // 2 + q * rem

        L = d - r
        R = d - l

        # Find the largest T for which jumping is faster
        low, high = L, R + 1

        while low < high:
            mid = (low + high) // 2

            if jump_time(mid) < normal_time:
                low = mid + 1
            else:
                high = mid

        K = low - 1

        ans = 0

        # Sum minimum times for jump-based journeys
        if K >= L:
            count = K - L + 1

            sum_T = (L + K) * count // 2
            sum_q = prefix(K - a) - prefix(L - 1 - a)

            jump_sum = sum_T + count + 2 * b * sum_q
            ans += jump_sum

        # Remaining jump lengths use normal movement
        total_count = R - L + 1
        jump_count = max(0, K - L + 1)
        normal_count = total_count - jump_count

        ans += normal_count * normal_time

        return ans % MOD
