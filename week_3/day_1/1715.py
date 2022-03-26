# https://www.acmicpc.net/problem/1715

# 주어진 카드묶음을 합치야한다.
# 합칠때는 두 묶음 단위로 합칠 수 있으며,
# 한번 합칠때는 각 묶음의 카드 수량을 더한 만큼 비교를 하여야한다.
# *A묶음(30장) + B묶음(20장) => 비교 50번
# 입력된 카드 묶음을 최소한으로 비교한다면 몇번 비교하여야하는가?
import heapq

N = int(input())
heap = []

# 입력값을 우선순위 큐에 넣는다.
for _ in range(N):
    heapq.heappush(heap, int(input()))

answer = 0
# 카드묶음이 1개가 될때까지 반복한다.
while N > 1:
    # 최소량의 2개의 묶음을 뽑고 합친다.
    A = heapq.heappop(heap)
    B = heapq.heappop(heap)
    AB = A + B
    # 합친 카드를 우선순위 큐에 넣는다.
    # 기존의 최소량보다, 합친량이 더 작거나 클 수 있으니 우선순위큐를 사용한것이다.
    heapq.heappush(heap, AB)

    # 총 비교량을 보관한다.
    answer += AB

    # 남은 카드 묶음을 계산한다.
    N -= 1

print(answer)
