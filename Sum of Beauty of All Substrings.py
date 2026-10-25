class Solution:
    def beautySum(self, s):
        # Code here
        # Here it is asking the All substring
        
        n = len(s)
        map = {}
        sums = 0
        for i in range(n):
            map.clear()
            for j in range(i,n):
                map[s[j]] = map.get(s[j], 0) + 1
                res = max(map.values()) - min(map.values())
                sums = sums + res
        return sums
