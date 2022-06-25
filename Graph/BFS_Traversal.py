from collections import deque

#Building Graph using Adjancency List Reperesentation
def build_graph(n, edges):
    graph = dict()
    print(n)
    for v in range(n):
        graph[v] = list()
    print(graph)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph
  
#BFS Function
def bfs(n, graph):
    q = deque()
    visited = [False]*n
    q.append(0)   #Marking 0 as start node and pushing it into the Queue
    visited[0] = True   #Marking 0 as visited
    bfs_list = []
    while q:
        curr_node = q.popleft()
        bfs_list.append(curr_node)

        for nbr in graph[curr_node]:
            if not visited[nbr]:
                visited[nbr] = True
                q.append(nbr)
    
    return bfs_list

#Driver Main Functon
if __name__ == "__main__":
    vertices = int(input("Number of Vertices : "))
    e = int(input("Number of Edges : "))
    edges = list()
    for i in range(e):
        u, v = map(int, input().split())
        edges.append((u,v))
    
    visited = [False]*vertices
    graph = build_graph(vertices, edges)
    
    #calling BFS Function
    print("BFS Traversal : ", bfs(vertices, graph))

    

