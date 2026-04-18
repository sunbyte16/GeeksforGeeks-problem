class Solution:
    def isBalanced(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            # If opening bracket → push
            if ch in '({[':
                stack.append(ch)
            else:
                # If stack empty or mismatch → invalid
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
        
        # If stack empty → balanced
        return len(stack) == 0
