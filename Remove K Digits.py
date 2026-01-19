class Solution:
    def removeKdig(self, s, k):
        stack = []

        for ch in s:
            # Remove larger digits from stack if possible
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # If removals still left, remove from end
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        # If empty, return "0"
        return result if result else "0"
