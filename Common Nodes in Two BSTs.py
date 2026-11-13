''' 
Structure of a Binary Search Tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findCommon(self, r1, r2):
        def inorder(root):
            stack = []
            result = []
            curr = root

            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left

                curr = stack.pop()
                result.append(curr.data)
                curr = curr.right

            return result

        a = inorder(r1)
        b = inorder(r2)

        i = j = 0
        ans = []

        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                ans.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1

        return ans
