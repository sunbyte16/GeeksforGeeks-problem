class Solution:
    def missingRange(self, arr, low, high):
        arr_set = set(arr)
        result = []
        
        for num in range(low, high + 1):
            if num not in arr_set:
                result.append(num)
        
        return result
