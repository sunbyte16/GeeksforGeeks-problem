class Solution:
    def lexicographicallyLargest(self, arr: list[int]) -> list[int]:
        # code here
        n = len(arr)
        i = 0

        while i < n:
            j = i
            while j + 1 < n and (arr[j] + arr[j + 1]) % 2 == 0:
                j += 1

            arr[i:j + 1] = sorted(arr[i:j + 1], reverse=True)
            i = j + 1

        return arr
