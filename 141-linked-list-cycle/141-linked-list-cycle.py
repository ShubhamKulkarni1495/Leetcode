# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        while head:
            if type(head.val) is bool:
                return True

            head.val = True
            head = head.next
        return False