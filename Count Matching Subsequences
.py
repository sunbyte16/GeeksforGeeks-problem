class Solution:
    def countWays(self, s1, s2):
        from functools import cache
        @cache
        def dfs(i1=len(s1)-1,i2=len(s2)-1):
            nonlocal s1,s2
            if i1<0 or i2<0:
                return i2<0
            ret=dfs(i1-1,i2)
            if s1[i1]==s2[i2]:
                ret+=dfs(i1-1,i2-1)
            return ret%(10**9+7)
        return dfs()