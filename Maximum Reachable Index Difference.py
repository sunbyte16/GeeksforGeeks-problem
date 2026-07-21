class Solution:
    def maxIndexDifference(self, s):
        # code here
        start = end = -1
        max_c_i = -1
        for i, c in enumerate(s):
            c_i = ord(c)
            if c == "a":
                if max_c_i == -1:
                    start = end = i
                    max_c_i = c_i
            elif c_i - 1 <= max_c_i:
                end = i
                if c_i > max_c_i:
                    max_c_i = c_i
        return end - start if start > -1 else -1
