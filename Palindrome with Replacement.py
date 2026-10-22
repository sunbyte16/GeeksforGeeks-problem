class Solution:
    def minimumSum(self, s: str) -> int:
        s = list(s)
        low, high = 0, len(s) - 1
        total = 0

        while low < high:
            if s[low] != s[high]:
                if s[low] == '?':
                    s[low] = s[high]
                elif s[high] == '?':
                    s[high] = s[low]
                else:
                    return -1
            low += 1
            high -= 1

        prev = '?'
        for c in s:
            if c != '?':
                if prev != '?':
                    total += abs(ord(c) - ord(prev))
                prev = c

        return total
