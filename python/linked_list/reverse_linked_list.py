# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        save_list = None
        retrieve_list = head
        
        while retrieve_list is not None:
            tmp = retrieve_list.next
            retrieve_list.next = save_list
            save_list = retrieve_list
            retrieve_list = tmp
        return save_list
