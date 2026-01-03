class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None


class Solution:
    def merge(self, a, b):
        # If one list is empty
        if not a:
            return b
        if not b:
            return a

        # Pick the smaller value
        if a.data <= b.data:
            result = a
            result.bottom = self.merge(a.bottom, b)
        else:
            result = b
            result.bottom = self.merge(a, b.bottom)

        result.next = None  # Ensure next is removed
        return result

    def flatten(self, root):
        # Base case
        if not root or not root.next:
            return root

        # Recursively flatten the rest
        root.next = self.flatten(root.next)

        # Merge current list with flattened next list
        root = self.merge(root, root.next)

        return root
