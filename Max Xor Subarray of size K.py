class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        # prefix[i] = xor of arr[0..i-1]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        max_xor = 0
        for i in range(n - k + 1):
            curr = prefix[i + k] ^ prefix[i]
            if curr > max_xor:
                max_xor = curr

        return max_xor
