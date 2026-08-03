class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        # code here
        ans = float('-inf')
        #minv is the smallest accumulated number from 0..=i-k. it is initalized as 0
        s, minv = 0, 0
        for i in range(0, len(arr)):
            arr[i] += s
            s = arr[i]
            if i >= k:
                minv = min(arr[i-k], minv)
            if i >= k-1:
                ans = max(ans, arr[i]-minv)
        return ans
