def solve(arr, s):
    n = len(arr)
    dp = [[0]*(s+1) for i in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        for j in range(1, s+1):
            if j < arr[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i-1]]

    return dp[n][s]
        
if __name__ == '__main__':
    n, m = map(int,input().split())
    c = list(map(int, input().split()))
    ans = solve(c, n)
    print(ans)
