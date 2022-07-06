#1514. Path with Maximum Probability
#Can be solved Using Dijkstra Algorithm

class Solution:
    def build_graph(self, n, edges, prob):
        graph = defaultdict(list)
        for i in range(len(edges)):
            graph[edges[i][0]].append([edges[i][1], prob[i]])
            graph[edges[i][1]].append([edges[i][0], prob[i]])
        return graph
    
    def solve(self, n, graph, start, end):
        distance = [0]*n
        visited = [False]*n
        maxHeap = []
        distance[start] = 1
        heappush(maxHeap, (-1, start))
        
        while maxHeap:
            curr = heappop(maxHeap)
            prob, node = -curr[0], curr[1]
            visited[node] = True
            
            for nbr, cost in graph[node]:
                if prob * cost > distance[nbr]:
                    distance[nbr] = prob * cost
                    heappush(maxHeap, (-distance[nbr], nbr))
        return distance[end]
        
        
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = self.build_graph(n, edges, succProb)
        return self.solve(n, graph, start, end)
        
