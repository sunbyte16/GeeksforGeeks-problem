class Solution:
    def pythagoreanTriplet(self, arr):
        n = len(arr)
        
        # Square all numbers
        arr = [x * x for x in arr]
        
        # Store squares in set
        s = set(arr)
        
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] in s:
                    return True
        
        return False
