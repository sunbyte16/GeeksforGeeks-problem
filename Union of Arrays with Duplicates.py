class Solution:    
    def findUnion(self, a, b):
        # Using set to store unique elements
        union_set = set(a)
        
        # Add elements of b
        union_set.update(b)
        
        # Return as list (driver will sort)
        return list(union_set)
