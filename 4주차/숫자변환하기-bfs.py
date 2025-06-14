def solution(x,y,n):
    INF = 10 ** 9
    dp = [INF] * (y+1)
    dp[x] = 0

    for v in range(x,y+1):
        if dp[v] == INF:
            continue

        if v + n <= y:
            dp[v+n] = min(dp[v+n], dp[v] + 1)
        if v * 2 <= y:
            dp[v*2] = min(dp[v*2], dp[v]+1)
        if v * 3 <= y:
            dp[v*3] = min(dp[v*3], dp[v]+1)
    for i in range(x, y+1):
        if dp[i] == INF:
            continue
        if i + n <= y:
            dp[i+n] = min(dp[i+n] , dp[i] + 1)
    return dp[y] if dp[y] != INF else -1
