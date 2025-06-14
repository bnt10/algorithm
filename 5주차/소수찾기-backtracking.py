def solution(numbers):
    result = set()
    visited = [False] * len(numbers)

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True


    def dfs(path):
        if path:
            num = int(path)
            if is_prime(num):
                result.add(num)
        for i in range(len(numbers)):
            if not visited[i]:
                visited[i] = True
                dfs(path + numbers[i])      # 상태 확장
                visited[i] = False          # 상태 복원 (backtrack)

    dfs("")
    return len(result)
