class Solution:
    def minimumStep (self, n):
        # code here
        count = 0
        while n > 1:
            if n % 3 == 0:
                n //= 3
            else:
                n -= 1
            count += 1
        return count
