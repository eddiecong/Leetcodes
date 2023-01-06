# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        root1 = less_list = ListNode(0)
        root2 = large_list = ListNode(0)
        while head:
            if head.val < x:
                less_list.next = ListNode(head.val)
                less_list = less_list.next
            else:
                large_list.next = ListNode(head.val)
                large_list = large_list.next
            head = head.next
        less_list.next = root2.next
        return root1.next