def build_graph(vertices, edges):
    graph = dict()
    for i in range(vertices):
        graph[i] = []
    
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        graph[parent].append(child)
        graph[child].append(parent)
    
    return graph

def contains_cycle(vertices, edges):
    visited = [False]*vertices
    graph = build_graph(vertices, edges)

    for i in range(vertices):
        if(dfs(i, -1, visited, graph)):
            return True
    
    return False

def dfs(node, parent, visited, graph):
    visited[node] = True

    for nbr in graph[node]:
        if not visited[nbr]:
            if dfs(nbr, node, visited, graph):
                return True
        
        elif nbr != parent:
            return True
    
    return False


if __name__ == "__main__":
    vertices = 7
    edges = [[0,1],[0,4],[0,5],[1,2],[2,3],[4,5],[5,6]]
    print(contains_cycle(vertices, edges))

