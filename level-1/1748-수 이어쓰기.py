'''
문제
1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.

1234567891011121314151617181920212223...

이렇게 만들어진 새로운 수는 몇 자리 수일까? 이 수의 자릿수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N(1 ≤ N ≤ 100,000,000)이 주어진다.

출력
첫째 줄에 새로운 수의 자릿수를 출력한다.

예제 입력 1
5
예제 출력 1
5
예제 입력 2
15
예제 출력 2
21

5
12345

15
123456789101112131415

15

10 - 1 + 1 = 10 * 1
15 - 10 + 1 = 6 * 2

1 ~ 9 = 1자리
10 ~ 99 = 2자리
100 ~ 999 = 3자리

위 규칙을 코드 레벨로 옮겨보자

자리수는 = digit
시작 = start
합산 = total

입력값이 5

while 10 * digit <= 5:
   total += digits * (start * 10 - start)
   digits +=1
   start *= 10

151
'''

# import sys
# input = sys.stdin.readline
# n = int(input().strip())
# def solve(n):
#     total_digits = 0
#     digits = 1
#     start = 1
#     while start * 10 <= n:
#         count_in_group = start * 10 - start
#         total_digits += count_in_group * digits
#         digits += 1      # 다음 그룹은 한 자리 수가 늘어남 (예: 1자리 -> 2자리)
#         start *= 10      # 다음 그룹의 시작 숫자 (예: 1자리 -> 10)
#
#
#     total_digits += (n - start + 1) * digits
#     return total_digits



import sys
input = sys.stdin.readline

n = int(input().strip())

def solve(n):
    total_digits = 0
    base = 10
    digits = 1
    start = 1


    while start * base <= n:
        total_digits += (start * base - start) * digits
        digits += 1
        start *= base

    total_digits += (n - start + 1) * digits
    return total_digits
print(solve(n))

