def count(n, k):
    dp = [[[0]*(k+1) for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][i][1] = 1
    for i in range(1, n+1):
        for j in range(i, n+1):
            for p in range(1, k+1):
                for x in range(1, j+1):
                    for q in range(1, min(p, x)+1):
                        dp[j][p][i] += dp[x][q][i-1] * dp[j-x][p-q][1]
    return sum(dp[n][k][i] for i in range(1, n+1))