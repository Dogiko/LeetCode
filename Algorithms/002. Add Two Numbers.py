# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        ans = ListNode((l1.val + l2.val) % 10)
        plus = (l1.val + l2.val >= 10)
        temp_node = ans
        while (l1.next != None) or (l2.next != None):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
            sum = l1.val + l2.val + plus
            temp_node.next = ListNode(sum % 10)
            plus = (sum >= 10)
            temp_node = temp_node.next

        
        if plus:
            temp_node.next = ListNode(1)
        
        return ans