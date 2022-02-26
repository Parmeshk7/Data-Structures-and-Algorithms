#GeeksForGeeks
'''Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.'''

def subsetSum(arr, n, s):
    dp = [[0]*(s+1) for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for j in range(1, s+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
    
    return dp[n][s]


if __name__ == "__main__":
    #Take number of elements in array
    n = int(input())

    #Taking the elements of array
    arr = list(map(int, input().split()))

    #Taking the target Sum value
    target = int(input())

    #getting the result 
    ans = subsetSum(arr, n, target)
    print(ans)


