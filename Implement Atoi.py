class Solution:
    def myAtoi(self, s):
        i, n = 0, len(s)
        
        # Step 1: Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Handle sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Convert digits
        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Check overflow before adding
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num
