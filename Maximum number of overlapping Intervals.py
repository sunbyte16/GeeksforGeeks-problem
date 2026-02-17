class Solution:
    def overlapInt(self, arr):
        events = []
        
        for start, end in arr:
            events.append((start, 1))      # interval starts
            events.append((end + 1, -1))   # interval ends (inclusive)
        
        # Sort events by time
        events.sort()
        
        curr = 0
        ans = 0
        
        for _, val in events:
            curr += val
            ans = max(ans, curr)
        
        return ans
