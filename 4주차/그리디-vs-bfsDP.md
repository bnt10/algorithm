for i in range(START, END +1):
    if dp[i] == INF:
        continue

    for next in tansitions(i):
        dp[next] = min(dp[nxt], dp[i] + COST)
