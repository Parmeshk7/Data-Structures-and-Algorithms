#DFS TRAVERSAL OF UNDIRECTED GRAPH

#Building Graph using Adjacency List Representation
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


#DFS Recursive Function
def dfs(v, graph, visited, dfs_nodes):
    visited[v] = True
    dfs_nodes.append(v)

    for nbr in graph[v]:
        if not visited[nbr]:
            #Calling dfs function again on non-visited adjacent node of current node
            dfs(nbr, graph, visited, dfs_nodes)



if __name__ == "__main__":
    vertices = int(input("Number of Vertices : "))
    e = int(input("Number of Edges : "))
    edges = list()
    for i in range(e):
        u, v = map(int, input().split())
        edges.append((u,v))
    
    visited = [False]*vertices
    graph = build_graph(vertices, edges)
    
    dfs_list = list()
    #Calling DFS function from 0 as starting Node
    dfs(0, graph, visited, dfs_list)
    print("DFS Traversal : ",dfs_list)

 

    

