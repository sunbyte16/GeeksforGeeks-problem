class Solution:
    def longestKSubstr(self, s, k):
        from collections import defaultdict
        
        left = 0
        freq = defaultdict(int)
        max_len = -1
        
        for right in range(len(s)):
            freq[s[right]] += 1
            
            # Shrink window if distinct characters > k
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            
            # Update answer if exactly k distinct characters
            if len(freq) == k:
                max_len = max(max_len, right - left + 1)
        
        return max_len
