class Solution:
    def permuteDist(self, arr):
        result = []
        
        def backtrack(start):
            if start == len(arr):
                result.append(arr[:])  # copy
                return
            
            for i in range(start, len(arr)):
                arr[start], arr[i] = arr[i], arr[start]   # swap
                backtrack(start + 1)
                arr[start], arr[i] = arr[i], arr[start]   # backtrack
        
        backtrack(0)
        return result
