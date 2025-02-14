class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        temp = ListNode()
        tail = temp

        while l1 or l2 or carry:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            sum = x + y + carry
            carry = sum // 10

            if sum > 9:
                sum -= 10
            
            newNode = ListNode(sum) # List node is predefined in the problem
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        res = temp.next

        return res
