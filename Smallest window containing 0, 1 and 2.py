class Solution:
    def smallestSubstring(self, s):
        count = [0, 0, 0]  # for '0', '1', '2'
        left = 0
        unique = 0
        min_len = float('inf')
        
        for right in range(len(s)):
            idx = ord(s[right]) - ord('0')
            
            if count[idx] == 0:
                unique += 1
            count[idx] += 1
            
            # valid window
            while unique == 3:
                min_len = min(min_len, right - left + 1)
                
                left_idx = ord(s[left]) - ord('0')
                count[left_idx] -= 1
                
                if count[left_idx] == 0:
                    unique -= 1
                
                left += 1
        
        return min_len if min_len != float('inf') else -1
