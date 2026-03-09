class Solution:
    def largestSwap(self, s):
        s = list(s)
        n = len(s)
        
        # Store last occurrence of each digit
        last = [-1] * 10
        
        for i in range(n):
            last[int(s[i])] = i
        
        for i in range(n):
            current = int(s[i])
            
            # Check for larger digit
            for d in range(9, current, -1):
                if last[d] > i:
                    # Swap
                    s[i], s[last[d]] = s[last[d]], s[i]
                    return "".join(s)
        
        return "".join(s)
