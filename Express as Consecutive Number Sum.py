class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        # Returns False if n is a power of 2, otherwise True
        return (n & (n - 1)) != 0
