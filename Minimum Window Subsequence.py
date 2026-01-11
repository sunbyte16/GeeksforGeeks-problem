class Solution:
    def minWindow(self, s1, s2):
        len_s1, len_s2 = len(s1), len(s2)
        if len_s2 == 0 or len_s2 > len_s1:
            return ""
        
        dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        
        for i in range(1, len_s1 + 1):
            for j in range(1, len_s2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = i if j == 1 else dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        start_index = 0
        min_length = len_s1 + 1
        
        for i in range(1, len_s1 + 1):
            if s1[i - 1] == s2[-1] and dp[i][len_s2] != 0:
                window_start = dp[i][len_s2] - 1
                window_length = i - window_start
                if window_length < min_length:
                    min_length = window_length
                    start_index = window_start
        
        return "" if min_length > len_s1 else s1[start_index:start_index + min_length]
