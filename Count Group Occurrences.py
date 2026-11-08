class Solution:
    def getCount (self, s, k):
        # code here
        groups = [0]*26
        n = len(s)
        i = 0
        while i < n:
            ch = s[i]
            groups[ord(ch)-ord('a')] += 1
            while i < n and ch == s[i]:
                i += 1

        return sum(1 for c in groups if c == k)
