## 2020/10/14

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        nodes = dict()
        while head:
            if head in nodes:
                return head
            else:
                nodes[head] = 1
                head = head.next
        return None
