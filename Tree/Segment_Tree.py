def build(node, start, end, tree, arr):
    if start == end:
        tree[node] = arr[start]
        return
    
    mid = (start + end)//2
    build(2*node+1, start, mid, tree, arr)
    build(2*node+2, mid+1, end, tree, arr)

    tree[node] = tree[2*node+1] + tree[2*node+2]

def query(node, start, end, left, right, tree):
    if end < left or start > right:
        return 0
    
    if left <= start and right >= end:
        return tree[node]
    
    mid = (start + end)//2
    return query(2*node+1, start, mid, left, right, tree) + query(2*node+2, mid+1, end, left, right, tree)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [0]*(4*n + 1)
    build(0, 0, n-1, tree, arr)
    print(tree)

    

