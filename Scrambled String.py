class Solution:
    def isScramble(self, S1: str, S2: str):
        memo = {}
        
        def solve(a, b):
            if a == b:
                return True
            
            if (a, b) in memo:
                return memo[(a, b)]
            
            # Pruning: if characters don't match
            if sorted(a) != sorted(b):
                memo[(a, b)] = False
                return False
            
            n = len(a)
            
            for i in range(1, n):
                # Case 1: No swap
                if solve(a[:i], b[:i]) and solve(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True
                
                # Case 2: Swap
                if solve(a[:i], b[n-i:]) and solve(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True
            
            memo[(a, b)] = False
            return False
        
        return solve(S1, S2)
