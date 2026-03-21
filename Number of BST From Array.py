class Solution:
    def countBSTs(self, arr):
        n = len(arr)
        
        # Precompute Catalan numbers up to n
        catalan = [0] * (n + 1)
        catalan[0] = 1
        catalan[1] = 1
        
        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]
        
        result = []
        
        for i in range(n):
            root = arr[i]
            
            # count smaller and greater elements
            left = sum(1 for x in arr if x < root)
            right = sum(1 for x in arr if x > root)
            
            result.append(catalan[left] * catalan[right])
        
        return result
