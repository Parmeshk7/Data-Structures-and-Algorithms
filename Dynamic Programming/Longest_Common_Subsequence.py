if __name__ == "__main__":    
    s = input() #FIRST STRING   
    t = input() #SECOND STRING
    m = len(s)  
    n = len(t)
    dp = [[0]*(n+1) for i in range(m+1)]    #DP for maintaining Length
    trace = [[None]*(n+1) for i in range(m+1)] #DP for tracing the path for LCS
    lcs = ""

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                trace[i][j] = "\>"
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                    trace[i][j] = "|"
                else:
                    dp[i][j] = dp[i][j-1]
                    trace[i][j] = "->" 

    #printing LCS
    while m > 0 and n > 0:
        if trace[m][n] == "\>":
            lcs = s[m-1] + lcs
            m = m-1
            n = n-1
        elif trace[m][n] == "|":
            m = m-1
        else:
            n = n-1

    print(lcs) 



