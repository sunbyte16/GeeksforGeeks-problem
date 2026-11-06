class Solution:
    def countBT(self, h: int) -> int:
            # code here

            if h == 1 or h == 0:
                return 1

            M = 1_000_000_000+7

            a0, a1 = 1, 1 
            for _ in range(2, h+1):
                a1, a0 = ((a1*a0*2)%M + a1*a1%M)%M, a1

            return a1
        
