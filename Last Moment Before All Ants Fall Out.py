class Solution:
    def getLastMoment(self, n, left, right):
        last = 0
        
        for pos in left:
            last = max(last, pos)
        
        for pos in right:
            last = max(last, n - pos)
        
        return last
