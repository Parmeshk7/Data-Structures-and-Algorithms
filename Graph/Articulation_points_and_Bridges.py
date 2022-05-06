#Articulation Points and Bridges

from collections import defaultdict


def solve(node, parent, vis, dis, low, graph, ap, br, timer):
    vis[node] = True
    dis[node] = timer
    low[node] = timer
    timer += 1
    child = 0
    for nbr in graph[node]:
        if nbr == parent:
            continue
        elif vis[nbr] is not True:
            solve(nbr, node, vis, dis, low, graph, ap,br, timer)
            child += 1
            low[node] = min(low[node], low[nbr])

            if low[nbr] >= dis[node] and parent != -1:
                ap.add(node)
            if low[nbr] > dis[node]:
                br.add((node, nbr))

        else:
            #Backedge
            low[node] = min(low[node], dis[nbr])

    if child >= 2 and parent == -1:
        ap.add(node)
    

def find_articulation_points(edges, vertices):
    visited = [False]*vertices
    discovery_time = [0]*vertices
    lowest_time = [0]*vertices
    graph = build_graph(edges)
    points = set()
    timer = 0
    br = set()

    for node in range(vertices):
        if visited[node] is not True:
            solve(node, -1, visited, discovery_time, lowest_time, graph, points, br, timer)

    return (points, br)


def build_graph(edges):
    graph = defaultdict(list)
    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u].append(v)
        graph[v].append(u)
    
    return graph


if __name__ == "__main__":
    vertices = int(input())
    m = int(input())
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append([u, v])
    
    print(find_articulation_points(edges, vertices))

    
    
