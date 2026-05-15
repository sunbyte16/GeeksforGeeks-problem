class Solution:
    def optimalKeys(self, n):
        keys=[0]*(n+1)
        for i in range(1,min(7,n+1)):
            keys[i]=i
        for i in range(7,n+1):
            for j in range(i-3):
                keys[i]=max(keys[i],(keys[j]*(i-j-1)))
        return keys[n]
