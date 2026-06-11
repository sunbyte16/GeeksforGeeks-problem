class Solution:
    def findIndex(self, s):
        n=len(s)
        close=s.count(")")
        open=0
        for i in range(n):
            if open==close:
                return i
            if s[i]=="(":
                open+=1
            else:
                close-=1
        return n
