# Definition for singly-linked list.
from typing import Optional


class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentnode , prevnode = head ,None
        while currentnode is not None:
            tempnode = currentnode.next
            currentnode.next = prevnode
            prevnode = currentnode
            currentnode = tempnode
        return prevnode