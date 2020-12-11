## 2020/12/11

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        length = len(nodes)
        visited = [0] * length
        visited[0] = 1
        last_index = 0
        for i in range(length // 2):
            next_index = length - 1 - i
            if next_index < 0 or next_index >= length or visited[next_index]: break
            nodes[i].next = nodes[next_index]
            visited[next_index] = 1
            last_index = next_index
            
            next_index = i + 1
            if next_index < 0 or next_index >= length or visited[next_index]: break
            nodes[length - 1 - i].next = nodes[next_index]
            visited[next_index] = 1
            last_index = next_index
        nodes[last_index].next = None