class Solution:
    def solve(self, n, s):
        # code here
        ret=0
        seen=set()
        assg=set()
        for c in s:
            if c in seen:
                seen.discard(c)
                assg.discard(c)
                continue
            seen.add(c)
            if len(assg)>=n:
                ret+=1
            else:
                assg.add(c)
        return ret
