#743. Network Delay Time

def build_graph(vertices, edges):
    graph = [[-1]*(vertices+1) for i in range(vertices+1)]
    
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
    
    return graph
    
    
def dijkstra(vertices, edges, src):
    dist = [math.inf]*(vertices+1)
    visited = [False]*(vertices + 1)
    parent = [-1]*(vertices + 1)
    graph = build_graph(vertices, edges)
    
    min_heap = []
    heappush(min_heap, (0, src))
    dist[src] = 0
    
    while min_heap:
        curr_dist, curr_node = heappop(min_heap)
        
        if not visited[curr_node]:
            visited[curr_node] = True
            for nbr in range(1, vertices+1):
                if graph[curr_node][nbr] != -1:
                    if curr_dist + graph[curr_node][nbr] < dist[nbr]:
                        dist[nbr] = curr_dist + graph[curr_node][nbr]
                        heappush(min_heap, (dist[nbr], nbr))
    
    ans = max(dist[1:])
    if ans == math.inf:
        return -1
    return ans
                
    
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return dijkstra(n, times, k)
      
      
        
