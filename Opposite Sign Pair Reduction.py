class Solution:
    def reducePairs(self, arr):
        stack = []
        
        for num in arr:
            while stack and stack[-1] * num < 0:
                top = stack[-1]
                
                if abs(top) > abs(num):
                    break
                elif abs(top) < abs(num):
                    stack.pop()
                else:
                    stack.pop()
                    break
            else:
                stack.append(num)
        
        return stack
