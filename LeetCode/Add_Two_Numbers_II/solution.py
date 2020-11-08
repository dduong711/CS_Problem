# solution.py

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode()
        l1_ = l1
        l2_ = l2
        ll1 = ll2 = 0
        while l1_ != None:
            ll1 += 1
            l1_ = l1_.next
        while l2_ != None:
            ll2 += 1
            l2_ = l2_.next
        n = self.add(ll1-ll2, l1, l2, l)
        if n != 0:
            l_ = ListNode(n)
            l_.next = l
            l = l_
        return l
    
    def add(self, diff, l1, l2 , l):
        if l1 != None and l2 != None:
            if l1.next != None or l2.next != None:
                ne = ListNode()
                l.next = ne
            if diff < 0:
                n = l2.val + self.add(diff+1, l1, l2.next, l.next)
            elif diff > 0:
                n = l1.val + self.add(diff-1, l1.next, l2, l.next)
            else:
                n = l1.val + l2.val + self.add(diff, l1.next, l2.next, l.next)
            l.val = n%10;
            return n//10
        return 0
