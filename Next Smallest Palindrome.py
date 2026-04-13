class Solution:
    def nextPalindrome(self, num):
        n = len(num)
        
        if all(d == 9 for d in num):
            return [1] + [0]*(n-1) + [1]
            
        v = num[:]
        
        # Step 1: Mirror
        for i in range(n//2):
            v[n-i-1] = v[i]
        
        if v > num:
            return v
        
        # Step 2: Increment middle
        i = (n-1)//2
        while i >= 0:
            if num[i] != 9:
                num[i] += 1
                break
            else:
                num[i] = 0
                i -= 1
        
        # Step 3: Mirror again
        for i in range(n//2):
            num[n-i-1] = num[i]
        
        return num
