# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedHead = None
        curr = None

        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    s = list1
                    list1 = list1.next
                else:
                    s = list2
                    list2 = list2.next
            elif list1:
                s = list1
                list1 = list1.next
            else:
                s = list2
                list2 = list2.next

            if not mergedHead:
                mergedHead = s
            if not curr:
                curr = s
            else:
                curr.next = s
                curr = s

        return mergedHead