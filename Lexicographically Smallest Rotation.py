class Solution:
    def lexiString(self, s: str) -> str:
        # code here
        n = len(s)
        t = s + s
        i = 0
        j = 1
        k = 0

        while i < n and j < n and k < n:
            if t[i + k] == t[j + k]:
                k += 1
                continue

            if t[i + k] > t[j + k]:
                i = i + k + 1
            else:
                j = j + k + 1

            if i == j:
                j += 1

            k = 0

        start = min(i, j)
        return t[start:start + n]
