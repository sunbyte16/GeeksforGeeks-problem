class Solution:
    def palindromePair(self, arr):

        n = len(arr)

        # Check palindrome
        def isPal(s):
            return s == s[::-1]

        # Store words with index
        mp = {}

        for i in range(n):
            mp[arr[i]] = i

        for i in range(n):

            word = arr[i]
            m = len(word)

            for j in range(m + 1):

                left = word[:j]
                right = word[j:]

                # Case 1
                if isPal(left):

                    rev = right[::-1]

                    if rev in mp and mp[rev] != i:
                        return True

                # Case 2
                if j != m and isPal(right):

                    rev = left[::-1]

                    if rev in mp and mp[rev] != i:
                        return True

        return False
