'''
Structure of linked list node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def compute(self,head):
        # code here
         # Function to reverse linked list
        def reverse(head):
            prev = None
            curr = head
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            return prev
        
        # Reverse the list
        head = reverse(head)
        
        # Remove nodes having smaller value than max seen so far
        max_so_far = head.data
        curr = head
        
        while curr and curr.next:
            if curr.next.data < max_so_far:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_so_far = curr.data
        
        # Reverse again to restore order
        return reverse(head)
