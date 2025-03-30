'''
춘향이는 편의점 카운터에서 일한다.


손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다.
동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.

예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를,
거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.


입력 : 정수 N(거스름 돈)
출력 : 2원과 5원으로 구성된 최소 동전 개수 , 불간능하면 -1
조건:  동전 개수는 최소 , 총합이 정확히 N 이 되어야 함


'''

# n = int(input())
#
# # 5원 동전을 최대한 많이 써보는 시도
# for five in range(n // 5, -1, -1):  # 5원 개수를 줄여가며 확인
#     rest = n - (five * 5)  # 남은 금액
#     if rest % 2 == 0:  # 나머지가 2원으로 나눠떨어지면 가능
#         two = rest // 2
#         print(five + two)  # 최소 동전 개수
#         break
# else:
#     # for-else: break 한 번도 안 걸렸으면 실행
#     print(-1)
#


"""
문제
오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

출력
첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.


입력 : x(1 <= x <= 12) , y(1  <= y <= 31)
출력 : 요일출력 (SUN, MON, TUE, WED, THU, FRI, SAT)
제약 : 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

x = 1  
y = 1
Mon

x = 1
y = 2
TUE 

x = 1
y = 8
Mon

1 , 7 
1월 1일이 월요일 

2월 
1 thu
[mon, tue, wed,fri,set,sun] 

1 월 arr[0]

30 % 7 2+1
2 월 arr[3]
28 / 7 




"""
# month, day = map(int,input().split())
#
# total_days = 0
# count_days = ""
# week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
# n = 1
# while n < month:
#     if n in [1, 3, 5, 7, 8, 10, 12]:
#         total_days += 31
#     if n in [2]:
#         total_days += 28
#     if n in[ 4, 6, 9, 11]:
#         total_days += 30
#     n += 1
#
# count_days = week[(total_days + day) % 7]
# print(count_days)
#
#

# 입력 받기
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
