class Solution:
    def isBinaryPalindrome(self, n):
        b = bin(n)[2:]   # remove '0b'
        return b == b[::-1]
