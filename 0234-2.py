## 2021/05/14

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        right = self.findMiddle(head)
        tail = right
        left = head
        rev_right = self.reverse(right)
        copy_reverse = rev_right
        while left and left != tail:
            if left.val != rev_right.val:
                return False
            left = left.next
            rev_right = rev_right.next
        self.reverse(copy_reverse)
        return True

    def findMiddle(self, head):
        if not head: return None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        if not head: return None
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    print("Is palindrome: " + str(Solution().isPalindrome(head)))

    head.next.next.next.next.next = ListNode(2)
    print("Is palindrome: " + str(Solution().isPalindrome(head)))

if __name__ == '__main__':
    main()