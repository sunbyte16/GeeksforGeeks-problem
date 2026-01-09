class Solution:
    def countAtMostK(self, arr, k):
        if k == 0:
            return 0

        freq = {}
        left = 0
        distinct = 0
        result = 0

        for right in range(len(arr)):
            # Add current element
            if arr[right] not in freq or freq[arr[right]] == 0:
                distinct += 1
            freq[arr[right]] = freq.get(arr[right], 0) + 1

            # Shrink window if distinct elements exceed k
            while distinct > k:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    distinct -= 1
                left += 1

            # Count subarrays ending at right
            result += (right - left + 1)

        return result
