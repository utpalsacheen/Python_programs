"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition of a singley linked list
# Definition for singly-linked list.
#class ListNode(object):
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
        str1 = ""
        str2 = ""
        cur = l1
        while cur != None:
            str1 = str1 + str(cur.val)
            cur = cur.next

        cur = l2
        while cur != None:
            str2 = str2 + str(cur.val)
            cur = cur.next


        sum_total  = int(str1) + int(str2)
        sum1 = str(sum_total)
        head = ListNode(int(sum1[0]))
        for i in range(len(sum1) - 1):
            cur = ListNode(int(sum1[i+1]))
            cur.next = head
            head = cur
        
        return head
        
