class Solution:
    def findKthSmall(self, arr, k):
        # code here

        arr.sort()  # replace it with arr=sorted(set(arr)) for the case where duplicate elements are there in the input arr
        n = len(arr)
        # First element (smallest after sorting) itself is greater than k 
        if k < arr[0]:
            return k
        # Last element (largest after sorting) itself is smaller than k + n (assuming there are no repeated elements, else set can be used before sorting)
        if k +n > arr[-1]:
            return  k + n
        # First gap is removed 
        k -= arr[0] - 1
        # Compute and remove required gaps
        for i in range(1, n):
            gap = arr[i] - arr[i - 1] - 1

            if k <= gap:
                return arr[i - 1] + k

            k -= gap
