## 2020/12/10

# """
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
# """

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.buildGraph(node, {})

    def buildGraph(self, node, exist_dict):
        if not node: return None
        if node in exist_dict: return exist_dict[node]
        new_node = Node(node.val, [])
        exist_dict[node] = new_node
        for neighbor in node.neighbors:
            new_neighbor = self.buildGraph(neighbor, exist_dict)
            if new_neighbor:
                new_node.neighbors.append(new_neighbor)
        return new_node