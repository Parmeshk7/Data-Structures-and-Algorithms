#133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        graph = dict()
        q = deque([node])
        visited = set()
        
        while q:
            curr = q.popleft()
            if curr.val in visited:
                continue
            visited.add(curr.val)
            
            if curr.val not in graph:
                graph[curr.val] = Node(curr.val)
            
            for nbr in curr.neighbors:
                if nbr.val not in graph:
                    graph[nbr.val] = Node(nbr.val)
                graph[curr.val].neighbors.append(graph[nbr.val])
                q.append(nbr)
            
        return graph[node.val]
        
        
                
                
            
        
        
