#Dijkstra Algorithm : Single Source Sortest Path


from collections import defaultdict
import math
from heapq import heappop, heappush


def build_graph(edges):
    graph = defaultdict(list)
    cost = dict()
    for edge in edges:
        graph[edge[0]].append(edge[1])
        cost[(edge[0], edge[1])] = edge[2]

    return (graph, cost)

def dijkstra(vertices, edges, start):
    graph, cost = build_graph(edges)

    dist = [math.inf]*(vertices+1)
    parent = [-1]*(vertices+1)
    visited = [False]*(vertices+1)

    min_heap = []
    heappush(min_heap, (0, start))
    dist[start] = 0
    while min_heap:
        curr = heappop(min_heap)
        curr_dist = curr[0]
        curr_node = curr[1]

        if not visited[curr_node]:
            visited[curr_node] = True

            for nbr in graph[curr_node]:
                if curr_dist + cost[(curr_node, nbr)] < dist[nbr]:
                    dist[nbr] = curr_dist + cost[(curr_node, nbr)]
                    parent[nbr] = curr_node
                    heappush(min_heap, (dist[nbr], nbr))
        
    return dist[1:]


if __name__ == "__main__":
    v, e, source = map(int, input().split())
 
    edges = []
    for i in range(e):
        src, ch, wt = map(int, input().split())
        edges.append([src, ch, wt])
    
    print(dijkstra(v, edges, source))

# Input:
# 4 5    
# 1 2 2
# 1 3 9
# 1 4 14
# 2 3 9
# 3 4 2

# Output:
# [0, 2, 9, 11]



