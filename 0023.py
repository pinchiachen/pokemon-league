## 2020/08/17

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return None
        arr = []
        for node in lists:
            while node:
                arr.append(node.val)
                node = node.next
        arr.sort()
        if len(arr) == 0:
            return None
        node = ListNode(arr[0])
        res = node
        for i in range(1, len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return res
