class Solution:
    def minOperation(self, n):
        # code here
        return n.bit_length() + n.bit_count() - 1
