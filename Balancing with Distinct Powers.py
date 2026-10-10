class Solution:
    def balancePan(self, a, b):
        # code here
        while b >  0:
            r = b % a
            
            if r == 0:
                b //= a
            elif r == 1:
                b = (b - 1) // a
            elif r == a - 1:
                b = (b + 1) // a
            else:
                return False
        
        return True
