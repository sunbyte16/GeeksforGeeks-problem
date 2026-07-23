class Solution:
    def canRepresentBST(self, arr):
        # code here
        stack = []
        lower_bound = float('-inf')
        for value in arr:

            if value < lower_bound:

                return False

            while stack and value > stack[-1]:

                lower_bound = stack.pop()

            stack.append(value)

        return True
