class Solution:
    def addTwoLists(self, head1, head2):

        # Helper to remove leading zeros
        def stripZeros(head):
            while head and head.data == 0:
                head = head.next
            return head if head else Node(0)

        # Helper to reverse a linked list
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # Step 1: remove leading zeros
        head1 = stripZeros(head1)
        head2 = stripZeros(head2)

        # Step 2: reverse both lists
        head1 = reverseList(head1)
        head2 = reverseList(head2)

        carry = 0
        dummy = Node(0)
        curr = dummy

        # Step 3: add digits
        while head1 or head2 or carry:
            val1 = head1.data if head1 else 0
            val2 = head2.data if head2 else 0

            total = val1 + val2 + carry
            carry = total // 10

            curr.next = Node(total % 10)
            curr = curr.next

            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next

        # Step 4: reverse result back
        result = reverseList(dummy.next)

        return result

