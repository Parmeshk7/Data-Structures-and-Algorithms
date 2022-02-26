def solve(arr, i, out, res):
    if i == len(arr):
        res.append(out[:])
        return
    
    out.append(arr[i])
    solve(arr, i+1, out, res)
    out.pop()
    solve(arr, i+1, out, res)


if __name__ == "__main__":
    subsets = list()

    #Input of array elements
    arr = list(map(int, input().split()))

    solve(arr, 0, [], subsets)
    print(subsets)


