class Solution:
    def getCount(self, n):
        # code here 
        parts = 2
        base = n - 1
        count = 0
        while base >= parts:
            if base % parts == 0:
                count += 1
            # The next part will be "part" numbers
            # higher than the first one.
            base -= parts
            parts += 1
        return count
