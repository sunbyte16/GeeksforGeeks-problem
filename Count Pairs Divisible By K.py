class Solution:
    def countKdivPairs(self, arr, k):
        # code here
        freq = [0]*k
        for x in arr: 
            freq[x%k]+=1
        ans = freq[0]*(freq[0]-1)//2
        for i in range(1,(k+1)//2):
            ans += freq[i]*freq[k-i]
        if k%2==0: 
            ans += freq[k//2]*(freq[k//2]-1)//2
        return ans
