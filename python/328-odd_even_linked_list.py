# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None or head.next==None:
            return head
        even_link = head.next
        head_link = head
        while True:
            if head.next.next==None:
                head.next = even_link
                return head_link
            else:
                next_current_node = head.next
                head.next = head.next.next
                head = head.next
                next_current_node.next = head.next
                if head.next==None:
                    head.next = even_link
                    return head_link
