"""
문제
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로,
각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서,
지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다.
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고,
50보다 작거나 같은 자연수이다.
둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

출력
첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW


-- 초안
입력 : M * N 크기의 보드 (검은색과, 흰색이 칠해져 있음) (  8 <=  N , M <= 50)
각 N 행 (B는  검은색, W 흰색)
출력 : 8 * 8 크기의 체스판 ( 다시 칠해야 하는 정사각형의 최소 개수)
제약 : 체스판은 검은색과 흰색이 번갈아서 칠해저 있음
변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다
체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

-- 개선안
입력 : N * M 크기의 보드 (문자 B 또는 W, 8 <= N, M <= 50)
출력 : 8x8 크기의 체스판으로 만들기 위해 다시 칠해야 하는 정사각형의 최소 개수
조건 :
 - 체스판은 흰/검 색이 번갈아야 하며, 인접한 칸은 다른색
 - 좌상단 횐색인 체스판 , 검정인 체스판 두 가지 경우를 모두 고려


아이디어 8부터 50까지
WB의 반복

BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB
BBBBBBBBB


10 * 10 이면

아이디어:
 1. M*N에 사각형이 몇개 있는가
 2. 가장 체스판 규칙(번갈아가면서 나와야한다)를 적게 틀린 조건


구현 :
 1. 반복문의 시작과 끝인 무엇 인지
 2. 8*8 수행을 별도 함수로 추출
 - 기대값이 아닌 경우 count += 1
 3 B , W 둘다 구하고 가장 작은 값을 선택
"""

# def count_paint(board, start_row, start_col, start_color):
#     count = 0
#     for i in range(8):
#         for j in range(8):
#             # 현재 좌표에서의 예상 색상
#             expected = start_color if (i + j) % 2 == 0 else ('B' if start_color == 'W' else 'W')
#             if board[start_row + i][start_col + j] != expected:
#                 count += 1
#     return count
#
# N,M = map(int, input().split())
# board = [input() for _ in range(N)]
#
# min_count = float('inf')
#
#
#
# for r in range(N - 7):
#     for c in range(M - 7):
#         backBoardCount = count_paint(board, r,c,"B")
#         whiteBoardCount = count_paint(board,r,c, "W")
#         min_count = min(min_count,backBoardCount,whiteBoardCount)
#
#
# print(min_count)


"""
문제요약 :
 입력 :
   brown  : 갈색 격자의 수,
   yellow : 노란색 격자의 수
 출력 :
   카펫의 가로, 세로 크기 순서대로 담은 배열 [width, height]
 조건 :
   테투리는 갈색 이고 중앙은 노란색
 제한사항 :
  8 <= brown <= 5000
  1 <= yellow <= 2,000,000
  width >= height
 
 
 
 아이디어 :
  1줄은 brown == 6 + (2 * yellow) 로 표현 가능
  그럼 언제 2줄로 바껴야 한는가?
  width >= height 는 최대 조건은 정사각형
  
  그렇다면 1:1 비율 최대 
  
  (brown - 6)/2 = yellow
  
  h = 
  
  카펫 크기: 가로 w, 세로 h
→ 내부(노란색) 크기: (w - 2) * (h - 2)
→ 테두리(갈색) 수: 전체 면적 - 노란색 = w * h - yellow
  
  1 1 1     1 1 1 1    1 1 1 1 1
  1 0 1     1 0 0 1    1 0 0 0 1
  1 1 1     1 1 1 1    1 1 1 1 1
  
  4 3
  
  for height in range(1, sqrt(yellow) + 1):
    if yellow % height == 0:
        width = yellow // height
  
 brown	yellow	return
    10	2	[4, 3]  5
    8	1	[3, 3]  8
    24	24	[8, 6]  1
    
입력을 다 더하면 타일 개수 

9 
"""

def solution(brown, yellow):
    total = brown + yellow

    for height in range(1, int(total ** 0.5) + 1):
        if total % height == 0:
            width = total // height

            # 노란색 영역은 (가로 - 2) * (세로 - 2)
            if (width - 2) * (height - 2) == yellow:
                return [width, height]

print(solution(8,1))

'''
  카펫 크기: 가로 w, 세로 h
→ 내부(노란색) 크기: (w - 2) * (h - 2)
→ 테두리(갈색) 수: 전체 면적 - 노란색 = w * h - yellow
  
'''