def solution(n):
    answer = 0

    def dfs(row, cols, diag1, diag2):
        nonlocal answer
        if row == n:
            answer += 1
            return
        for col in range(n):
            if col in cols:
                continue
            if (row - col) in diag1:
                continue
            if (row + col) in diag2:
                continue

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            dfs(row + 1, cols, diag1, diag2)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    dfs(0, set(), set(), set())
    return answer

