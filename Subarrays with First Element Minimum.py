class Solution:
    def countSubarrays(self, arr):
        n = len(arr)
        stack = []
        ans = 0
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                next_smaller = stack[-1]
            else:
                next_smaller = n
            
            ans += next_smaller - i
            stack.append(i)
        
        return ans
