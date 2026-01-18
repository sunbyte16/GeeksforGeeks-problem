class Solution:
    def nextFreqGreater(self, arr):
        from collections import Counter

        n = len(arr)
        freq = Counter(arr)
        stack = []
        res = [-1] * n

        for i in range(n - 1, -1, -1):
            # Remove elements with frequency <= current
            while stack and freq[stack[-1]] <= freq[arr[i]]:
                stack.pop()

            # If stack not empty, top has higher frequency
            if stack:
                res[i] = stack[-1]

            # Push current element
            stack.append(arr[i])

        return res
