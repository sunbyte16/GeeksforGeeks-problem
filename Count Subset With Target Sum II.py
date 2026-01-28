class Solution:
    def countSubset(self, arr, k):
        from bisect import bisect_left, bisect_right
        
        n = len(arr)
        mid = n // 2
        
        left = arr[:mid]
        right = arr[mid:]
        
        # Generate all subset sums of a list
        def subset_sums(nums):
            sums = [0]
            for num in nums:
                sums += [num + s for s in sums]
            return sums
        
        left_sums = subset_sums(left)
        right_sums = subset_sums(right)
        
        right_sums.sort()
        
        count = 0
        for s in left_sums:
            target = k - s
            # count occurrences of target in right_sums
            count += bisect_right(right_sums, target) - bisect_left(right_sums, target)
        
        return count
