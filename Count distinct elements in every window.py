class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        if k > n:
            return []

        freq = {}
        result = []

        # First window
        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0) + 1

        result.append(len(freq))

        # Remaining windows
        for i in range(k, n):
            # Remove outgoing element
            out_elem = arr[i - k]
            freq[out_elem] -= 1
            if freq[out_elem] == 0:
                del freq[out_elem]

            # Add incoming element
            freq[arr[i]] = freq.get(arr[i], 0) + 1

            result.append(len(freq))

        return result
