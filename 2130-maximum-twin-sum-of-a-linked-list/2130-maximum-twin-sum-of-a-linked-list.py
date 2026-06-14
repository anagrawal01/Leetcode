# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        aadha= []
        hh =fah= head
        while fah and fah.next:
            aadha.append(hh.val)
            hh=hh.next
            fah=fah.next.next
        quack = 0
        while hh:
            quack= max(quack, aadha.pop() + hh.val)
            hh = hh.next
        return quack
        