# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_0 = (l1.val + l2.val) % 10
        jw = int((l1.val + l2.val) // 10)
        result = ListNode(result_0)
        result.next = ListNode(jw)###用来存储结果的nodelist
        l1 = l1.next
        l2 = l2.next
        l3 = result ###指向result开头,最后返回
        while True:
            if l1 or l2:
                if l1 and l2:
                    sum_one = l1.val + l2.val + jw
                    l1 = l1.next
                    l2 = l2.next
                elif l1:
                    sum_one = l1.val + 0 + jw
                    l1 = l1.next
                else:
                    sum_one = l2.val + 0 + jw
                    l2 = l2.next
                jw = sum_one // 10
                sum_one = sum_one%10
                result.next.val = sum_one
                result.next.next = ListNode(jw)
                result = result.next
            else:
                if result.next.val==0:
                    result.next = None
                break
        return l3

##[2,4,3]
s1 = ListNode(2)
s1.next = ListNode(4)
s1.next.next = ListNode(3)
##[5,6,4]
s2 = ListNode(5)
s2.next = ListNode(6)
s2.next.next = ListNode(4)

s = Solution()
s.addTwoNumbers(s1,s2)
