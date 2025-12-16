class Solution:
    def areRotations(self, s1, s2):
        if len(s1) != len(s2):
            return False
        # if equal, or s2 appears in doubled s1, then rotation
        return s2 in (s1 + s1)
