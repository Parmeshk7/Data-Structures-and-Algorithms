#207. Course Schedule

class Solution:
    def build_graph(self, v, edges):
        graph = dict()
        for i in range(v):
            graph[i] = list()
        
        for edge in edges:
            graph[edge[1]].append(edge[0])
        
        return graph
    
    def get_indegree(self, v, edges):
        indegree = dict()
        for i in range(v):
            indegree[i] = 0
        
        for edge in edges:
            indegree[edge[0]] += 1
        
        return indegree
        
        
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        graph = self.build_graph(n, edges)
        indegree = self.get_indegree(n, edges)
        
        q = deque()
        for node in range(n):
            if indegree[node] == 0:
                q.append(node)
        
        order = list()
        while q:
            curr = q.popleft()
            order.append(curr)
            
            for nbr in graph[curr]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    q.append(nbr)
        
        if len(order) == n:
            return True
        return False
            
        
