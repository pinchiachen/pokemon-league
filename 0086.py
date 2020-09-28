## 2020/09/28

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head: return head
        greater_list = ListNode(0)
        dummy_greater = greater_list
        cur = ListNode(0)
        cur.next = head
        post = head
        dummy = cur
        while post:
            while post and post.val < x:
                post = post.next
                cur = cur.next
            while post and post.val >= x:
                greater_list.next = ListNode(post.val)
                greater_list = greater_list.next
                post = post.next
            if cur.next != post:
                cur.next = post
        cur.next = dummy_greater.next
        return dummy.next