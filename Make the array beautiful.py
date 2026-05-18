class Solution:
    def makeBeautiful(self, arr: list[int]) -> list[int]:
        # code here
        
        def same(a, b):
            if a == 0:
                return b >= 0
            if b == 0:
                return a >= 0
            return a*b > 0
        
        beautiful = []
        
        for num in arr:
            if beautiful and not same(beautiful[-1], num):
                beautiful.pop()
            else:
                beautiful.append(num)
            
        return beautiful
