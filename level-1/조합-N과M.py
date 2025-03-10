"""
문제
자연수 N과 M이 주어졌을때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

 - 1부터 N까지 자연수 중 에 중복 없이 M개를 고른 수열
 - 고른 수열은 오름차순이어야 한다.

입력
 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

예제 입력
 3 1
 예제 출력
 1
 2
 3
"""

from itertools import combinations
import sys
#M,N 입력 받기
input = sys.stdin.readline
def solve():
    N, M = map(int, input().split())

    for comb in combinations(range(1,N+1),M):
            print(' '.join(map(str,comb)))

solve()