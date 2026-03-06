class Solution:
    def minWindow(self, s, p):
        from collections import Counter
        
        if len(p) > len(s):
            return ""
        
        need = Counter(p)
        missing = len(p)
        left = 0
        
        min_len = float('inf')
        start = 0
        
        for right in range(len(s)):
            
            if need[s[right]] > 0:
                missing -= 1
            need[s[right]] -= 1
            
            while missing == 0:
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                
                left += 1
        
        if min_len == float('inf'):
            return ""
        
        return s[start:start + min_len]
