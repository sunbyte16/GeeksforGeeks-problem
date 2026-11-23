class Solution:
    def posInfinite(self, s: str, pos: int) -> str:
        # code here
        n = len(s)
        k = 0
        while n < pos:
            k += 1
            n = n*2 + k
        
        left = True
        while k > 0:
            n = (n-k)//2
            if pos > n and pos <= n+k:
                 return '$'
                 
            if pos > n+k:
                pos -= n+k
                left = False
            else:
                left = True
            k -= 1
            
        #print(f"{reversed = }, {pos = }")
        return s[pos-1] if left else s[n-pos]
