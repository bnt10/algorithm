def solution(word):
    letters = ['A', 'E', 'I', 'O', 'U']
    count = 0
    answer = 0

    def dfs(current):
        nonlocal count, answer
        if current == word:
            answer = count
            return
        if len(current) == 5:
            return
        for ch in letters:
            count += 1
            dfs(current + ch)
            if answer:  # 찾았으면 더 이상 탐색 X
                return

    dfs("")
    return answer

print(solution("AAAAE"))