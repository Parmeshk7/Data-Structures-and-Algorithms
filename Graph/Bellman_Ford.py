import math


def bellman_ford(n, edges, src):
    distance = [math.inf]*(n+1)
    distance[src] = 0

    for i in range(n-1):
        for edge in edges:
            u, v, c = edge[0], edge[1], edge[2]
            if distance[u] + c < distance[v]:
                distance[v] = distance[u] + c
            
    for edge in edges:
        u, v, c = edge[0], edge[1], edge[2]
        if distance[u] + c < distance[v]:
            return -1
    
    return distance[1:]


if __name__ == "__main__":
    vertices = int(input("Enter Number of Vertices : "))
    edges = list()
    e = int(input("Enter Number of Edges : "))
    for i in range(e):
        u, v, c = map(int, input().split())
        edges.append([u,v,c])
    
    res = bellman_ford(vertices, edges, 1)
    if res == -1:
        print("Graph contains Cycle")
    else:
        print(res)

