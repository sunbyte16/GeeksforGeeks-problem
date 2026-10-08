class Solution:
    def maxFrequency(self, arr, k):
        # code here
        arr.sort()
        start = max_len = sumi = 0
        for end in range(len(arr)):
            sumi += arr[end]
            while (l := end - start + 1) * arr[end] - sumi > k:
                sumi -= arr[start]
                start += 1
            if l > max_len:
                max_len = l
        return max_len
