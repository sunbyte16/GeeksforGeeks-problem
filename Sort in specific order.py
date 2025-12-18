class Solution:
    def sortIt(self, arr):
        odds = []
        evens = []
        for x in arr:
            if x % 2 == 1:
                odds.append(x)
            else:
                evens.append(x)

        odds.sort(reverse=True)  # odd numbers descending
        evens.sort()             # even numbers ascending

        res = odds + evens

        # IMPORTANT: modify arr in-place
        for i in range(len(arr)):
            arr[i] = res[i]
