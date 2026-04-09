class Solution:
    def intersection(self, a, b):
        i, j = 0, 0
        result = []
        
        while i < len(a) and j < len(b):
            # Skip duplicates in a
            if i > 0 and a[i] == a[i - 1]:
                i += 1
                continue
            
            # Skip duplicates in b
            if j > 0 and b[j] == b[j - 1]:
                j += 1
                continue
            
            if a[i] == b[j]:
                result.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1
        
        return result
