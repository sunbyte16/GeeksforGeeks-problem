from typing import List

class Solution:
    def increasingNumbers(self, n : int) -> List[int]:
        if n==1:
            return [i for i in range(10)]
        
        res = []
        
        def fun(pos, n, temp):
            if pos==n:
                res.append(int("".join([str(i) for i in temp])))
                return
            
            for i in range(1 if not pos else temp[pos-1]+1, 10):
                temp[pos] = i
                fun(pos+1, n, temp)
        
        fun(0, n, [0]*n)
        return res
