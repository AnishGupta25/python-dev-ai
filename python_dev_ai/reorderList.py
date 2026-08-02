# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast = head , head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        node1 = head
        node2 = slow.next
        slow.next = None

        node2 = self.reverseList(node2)
        node = ListNode(-1)
        current = node
        while node1 is not None or node2 is not None:
            if node1 is not None:
                current.next = node1
                node1 = node1.next
                current = current.next
            if node2 is not None:
                current.next = node2
                node2 = node2.next
                current = current.next
        
    def reverseList(self,Node):
        current , previous = Node , None
        while current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous