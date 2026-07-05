class Solution:

   def maxCharGap(self, s: str) -> int:
        seen = [-1]*26
        ans=0
        for i,c in enumerate(s):
            j = ord(c)-ord('a')
            if seen[j]==-1:
                seen[j] = i
            else:
                ans = max(ans,i-seen[j])
        return ans-1
