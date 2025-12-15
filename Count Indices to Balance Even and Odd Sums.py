class Solution:
    def cntWays(self, arr):
        n = len(arr)
        # prefix sums for original indices
        pref_even = [0] * (n + 1)
        pref_odd  = [0] * (n + 1)
        for i in range(n):
            pref_even[i + 1] = pref_even[i]
            pref_odd[i + 1]  = pref_odd[i]
            if i % 2 == 0:
                pref_even[i + 1] += arr[i]
            else:
                pref_odd[i + 1] += arr[i]

        total_even = pref_even[n]
        total_odd  = pref_odd[n]

        ans = 0
        for i in range(n):
            # sums on left side [0..i-1] keep same parity
            left_even = pref_even[i]
            left_odd  = pref_odd[i]

            # right side [i+1..n-1] shifts parity
            right_even_before = total_even - pref_even[i + 1]
            right_odd_before  = total_odd  - pref_odd[i + 1]

            # after shift: even indices on right come from old odd positions, and vice versa
            new_even = left_even + right_odd_before
            new_odd  = left_odd  + right_even_before

            if new_even == new_odd:
                ans += 1

        return ans
