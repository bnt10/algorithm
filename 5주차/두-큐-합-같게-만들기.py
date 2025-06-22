"""
1. 하나의 큐를 골라 원소를 추출(pop)
2. 추출된 원소를 다른 큐에 집어넣는(insert)
3. queue1 과 queue2 원소 합이 같도록
4. 필요 한 작업의 최소 횟수를 구하고자 할때 pop + insert 는 1회 작업

# 문제 풀이
1. target은 sum(q1+ q2) // 2
2. pop -> insert 함수 생성
3. ???
"""

from collections import deque
def solution(queue1, queue2):
    target = sum(queue1 +  queue2) // 2
    dq1 = deque(queue1)
    dq2 = deque(queue2)


    def pop_and_move(q1,q2):
        pop_item =  q1.popleft()
        q2.insert(len(q2),pop_item)
    pop_and_move(dq1,dq2)
    pop_and_move(dq2,dq1)

    print(dq1,dq2)
    answer =  -2
    return answer

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))