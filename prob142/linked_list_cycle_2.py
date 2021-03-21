# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        temp_dict = {}
        temp = head
        while temp is not None:
            if temp in temp_dict:
                return temp
            else:
                temp_dict[temp] = 1
            temp = temp.next
        return None
