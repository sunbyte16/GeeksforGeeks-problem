class Solution:
    def findMax(self, n):
        s = str(n)

        # Start with n itself
        ans = n
        max_sum = sum(int(d) for d in s)

        # Try numbers obtained by reducing one digit
        # and making all following digits 9
        for i in range(len(s)):
            if s[i] == '0':
                continue

            candidate_str = (
                s[:i] +
                str(int(s[i]) - 1) +
                '9' * (len(s) - i - 1)
            )

            candidate = int(candidate_str)
            digit_sum = sum(int(d) for d in candidate_str)

            if digit_sum > max_sum:
                max_sum = digit_sum
                ans = candidate
            elif digit_sum == max_sum and candidate > ans:
                ans = candidate

        return ans
