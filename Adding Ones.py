class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
        # code here
        ret=[0]*n
        for ix in updates:
            ret[ix-1]+=1
        for ix in range(1,n):
            ret[ix]+=ret[ix-1]
        return ret
