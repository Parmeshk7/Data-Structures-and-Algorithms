import math

def build_graph(n,edges):
    graph = [[-1]*n for i in range(n)]
    for edge in edges:
        graph[edge[0]][edge[1]] = edge[2]
        graph[edge[1]][edge[0]] = edge[2]
    
    return graph

def minKey(n, distance, mstSet):
    min_dist = math.inf
    selected = 0
    for i in range(n):
        if distance[i] < min_dist and mstSet[i] == False:
            min_dist = distance[i]
            selected = i
    
    return selected
    

def prims(n, graph):
    mstSet = [False]*n
    distance = [math.inf]*n

    distance[0] = 0

    for vertex in range(n):
        curr_node = minKey(n, distance, mstSet)
        mstSet[curr_node] = True

        for nbr in range(n):
            if mstSet[nbr] is False and graph[curr_node][nbr] != -1 and graph[curr_node][nbr] < distance[nbr]:
                distance[nbr] = graph[curr_node][nbr]
    print(distance)
    return sum(distance) 



if __name__ == "__main__":
    vertices = int(input("Enter Number of Vertices"))
    edges = list()
    n = int(input("Enter Number of Edges : "))
    for i in range(n):
        u, v, c = map(int, input().split())
        edges.append([u,v,c])
    
    print(edges)

    graph = build_graph(vertices, edges)

    print(prims(vertices, graph))
