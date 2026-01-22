class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)

        # --------- For Maximum ---------
        prev_greater = [-1] * n
        next_greater = [n] * n
        stack = []

        # Previous Greater
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            prev_greater[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Next Greater
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            next_greater[i] = stack[-1] if stack else n
            stack.append(i)

        max_sum = 0
        for i in range(n):
            left = i - prev_greater[i]
            right = next_greater[i] - i
            max_sum += arr[i] * left * right

        # --------- For Minimum ---------
        prev_smaller = [-1] * n
        next_smaller = [n] * n
        stack.clear()

        # Previous Smaller
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_smaller[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Next Smaller
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_smaller[i] = stack[-1] if stack else n
            stack.append(i)

        min_sum = 0
        for i in range(n):
            left = i - prev_smaller[i]
            right = next_smaller[i] - i
            min_sum += arr[i] * left * right

        return max_sum - min_sum
