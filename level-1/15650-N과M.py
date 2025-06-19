"""
문제 접근 :
 - 1부터 N 까지 자연수 중에서 중복 없이 M 개를 고른 수열 -> 조합
 - 고른 수열이 오름 차순

풀이 방법
  1. itertools의  combinations을 사용
  2. dfs + backtracking 사용

2번 방법으로 사용

 - 1 -> N 까지 배열 생성
 - visited 배열 생성
 - 종료조건 설정 -> M 개 선택
1 - > 2, 3

"""
import sys

def solution(n,m):
    arr = [i for i in range(1, n+1)]
    visited = [False] * n
    def dfs(i,path):
        if len(path) == m:
            print(*path)
            return
        for num in range(i,n):
            if not visited[num]:
                visited[num] = True
                path.append(arr[num])
                dfs(num+1,path)
                path.pop()
                visited[num] = False
    dfs(0,[])

n,m = map(int,input().split())
solution(n,m)


import sys

def combinations(n: int, m: int) -> list[str]:
    """1..n 중 m개 조합을 문자열로 반환"""
    out = []
    combo = []

    def backtrack(start: int) -> None:
        if len(combo) == m:
            out.append(" ".join(map(str, combo)))
            return
        for num in range(start, n + 1):
            combo.append(num)
            backtrack(num + 1)
            combo.pop()

    backtrack(1)
    return out


def main() -> None:
    n, m = map(int, sys.stdin.readline().split())
    sys.stdout.write("\n".join(combinations(n, m)))

if __name__ == "__main__":
    main()