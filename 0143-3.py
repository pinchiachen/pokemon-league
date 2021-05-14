## 2021/05/14

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        right = self.findMiddle(head)
        rev_right = self.reverse(right)
        while rev_right:
            left_next = head.next
            right_next = rev_right.next
            head.next = rev_right
            head = head.next
            head.next = left_next
            head = head.next
            rev_right = right_next
        head.next = None

    def findMiddle(self, head):
        if not head: return None
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow if not fast else slow.next

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
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    Solution().reorderList(head)

if __name__ == '__main__':
    main()