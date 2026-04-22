class Solution:
    def findMean(self, arr, queries):
        n = len(arr)
        
        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]
        
        result = []
        
        for l, r in queries:
            sub_sum = prefix[r + 1] - prefix[l]
            length = r - l + 1
            result.append(sub_sum // length)
        
        return result
