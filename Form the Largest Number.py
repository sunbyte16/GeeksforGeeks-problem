from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        # Convert to strings
        nums = [str(x) for x in arr]
        
        def compare(x, y):
            # Compare x+y vs y+x
            if x + y > y + x:
                return -1  # x before y
            elif x + y < y + x:
                return 1   # y before x
            else:
                return 0
        
        # Sort with custom comparator (descending order)
        nums.sort(key=cmp_to_key(compare))
        
        # Handle all zeros case
        if nums[0] == '0':
            return '0'
        
        # Join to form result
        return ''.join(nums)
