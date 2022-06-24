
def find_set(node, parent):
    if parent[node] == -1:
        return node
    return find_set(parent[node], parent)


def kruskal(n, edges):
    cost = 0
    parent = [-1]*n
    for edge in edges:
        parent_u = find_set(edge[0], parent)
        parent_v = find_set(edge[1], parent)

        if parent_u != parent_v:
            parent[parent_v] = parent_u
            cost += edge[2]
    
    return cost

if __name__ == "__main__":
    vertices = int(input("Enter Number of Vertices"))
    edges = list()
    n = int(input("Enter Number of Edges : "))
    for i in range(n):
        u, v, c = map(int, input().split())
        edges.append([u,v,c])
    
    print(edges)

    print("MST Cost : ", kruskal(vertices, sorted(edges, key=lambda x : x[2])))
