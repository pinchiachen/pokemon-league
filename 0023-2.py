## 2020/11/24
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        heapq.heapify(heap)
        [heapq.heappush(heap, (node.val, idx)) for idx, node in enumerate(lists) if node]
        dummy = ListNode(0)
        head = dummy
        while heap:
            cur_val, cur_idx = heapq.heappop(heap)
            cur_node = lists[cur_idx]
            head.next = cur_node
            head = head.next
            cur_node = cur_node.next
            lists[cur_idx] = cur_node
            if cur_node:
                heapq.heappush(heap, (cur_node.val, cur_idx))
        head.next = None
        return dummy.next
