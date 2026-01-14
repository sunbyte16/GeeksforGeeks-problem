class Solution:
    def catchThieves(self, arr, k):
        police = []
        thief = []
        
        # Collect positions
        for i, ch in enumerate(arr):
            if ch == 'P':
                police.append(i)
            else:
                thief.append(i)
        
        i = j = 0
        count = 0
        
        # Two-pointer greedy matching
        while i < len(police) and j < len(thief):
            if abs(police[i] - thief[j]) <= k:
                count += 1
                i += 1
                j += 1
            elif police[i] < thief[j]:
                i += 1
            else:
                j += 1
        
        return count
