class Solution:
    def minSubsets(self, arr):
        #code here
        s = set(arr)
        return sum(x - 1 not in s for x in s)
