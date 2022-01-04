class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        left = head
        right = head.next
        
        while left and right:
            right.next, left = left, right.next
            if left and right:
                left.next, right = right, left.next

        head.next = None
        return left or right