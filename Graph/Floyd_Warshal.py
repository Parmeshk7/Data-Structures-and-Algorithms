import math

#Building Graph using Adjancency Matrix Representation
def build_graph(n,edges):
    graph = [[-1]*(n) for i in range(n)]
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        #graph[edge[1]][edge[0]] = edge[2] #for Undirected Graph this statement will not be commented
    
    return graph

#Floyd Warshal Function
def floyd_warshal(n, graph):
    for i in range(n):
        for j in range(n):
            if i == j and graph[i][j] == -1:
                #marking diagonal as zero
                graph[i][j] = 0
            elif graph[i][j] == -1:
                #marking not connected nodes with infinite distance
                graph[i][j] = math.inf

    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == k or j == k:
                    continue
                if graph[i][k] != math.inf and graph[k][j] != math.inf:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

#Function to Print Graph
def printGraph(n, graph):
    for i in range(n):
        print(*graph[i])



#Driver Function 
if __name__ == "__main__":

    vertices = int(input("Enter Number of Vertices : "))
    edges = list()
    e = int(input("Enter Number of Edges : "))
    for i in range(e):
        u, v, c = map(int, input().split())
        edges.append([u,v,c])
    
    graph = build_graph(vertices, edges)
    print("Input Graph : ")
    printGraph(vertices ,graph)

    #Calling Floyd Warshal Function
    floyd_warshal(vertices, graph)
    print("All Pair Shortest Path : ")
    printGraph(vertices, graph)