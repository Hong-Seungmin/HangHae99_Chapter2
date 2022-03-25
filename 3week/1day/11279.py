# https://www.acmicpc.net/problem/11279

# 입력된 숫자들을 정렬하여, 큰 숫자부터 출력한다.
# 입력은 첫째 줄에 숫자의 개수 N 입력,
# *자연수는 정렬하여 보관, 0 이라면 출력을 의미 한다.
# 둘째 줄부터 N개의 숫자를 입력한다.
# 출력은 입력된 숫자 중 0 의 개수 만큼 출력한다.
import heapq
import sys

# 그냥 input()을 하면 시간초과가 되는듯 하다.
input = sys.stdin.readline

# N 입력
N = int(input())
heap = []

# N개의 숫자 입력
# 0이면 출력,
# 자연수이면 힙에 보관.
for _ in range(N):
    num = int(input())
    # 입력값이 0이면,
    # 힙의 값을 출력. ( 없다면, 0 출력 )
    if num == 0:
        # 힙에 값이 들어있다면,
        # 값을 꺼내어 출력
        if heap:
            print((-1) * heapq.heappop(heap))
        # 힙에 값이 없다면,
        # 0을 출력
        else:
            print(0)
    # 입력값이 자연수라면,
    # 입력값을 힙에 저장.
    else:
        heapq.heappush(heap, (-1) * num)
