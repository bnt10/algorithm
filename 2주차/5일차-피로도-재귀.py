def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n

    def dfs(cur_k):
        max_done = 0
        for i in range(n):
            if not visited[i]:
                need, cost = dungeons[i]
                if cur_k >= need:
                    visited[i] = True
                    # 이 던전을 돌고 나서 얻은 최대치
                    done = 1 + dfs(cur_k - cost)
                    visited[i] = False
                    # 여러 선택지 중 최댓값 취합
                    if done > max_done:
                        max_done = done
        return max_done

    return dfs(k)
