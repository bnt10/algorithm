'''

문제
오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

출력
첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

입력: 두 정수 x, y (x = 월, y = 일)
출력: 그 날짜가 무슨 요일인지 (MON, TUE, ..., SUN 중 하나)
조건: 2007년은 윤년이 아님, 1월 1일은 MON
'''

x, y = map(int, input().split())  # x: 월, y: 일

# 각 달의 일 수 (2007년은 윤년 아님)
month_days = [31, 28, 31, 30, 31, 30,
              31, 31, 30, 31, 30, 31]

# 요일 리스트 (1월 1일이 월요일)
week = [ 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

# 1월 1일부터 x월 y일까지 총 며칠 지났는지 계산
total_days = sum(month_days[:x - 1]) + y

# 요일 계산
print(week[total_days % 7])

sum(month_days[:x-1])