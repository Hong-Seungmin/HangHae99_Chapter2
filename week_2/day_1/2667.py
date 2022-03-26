# https://www.acmicpc.net/problem/2667

from typing import List


# 정사각형으로 주어진 지도에서 0은 땅 1은 집을 나타낸다.
# 지도에서 상하좌우에 집이 존재한다면 그 집들은 같은 단지이다.
# 좌표의 가로세로 크기를 정수 n을으로 입력한 뒤,
# 각 좌표의 표시를 str배열로 입력한다.
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
# 출력값은 총 단지의 수와 각 단지의 집의 수를 오름차순으로 출력하라.
# 3
# 7
# 8
# 9

# dfs를 스택으로 풀어보았다.
def solution(inner_map: List[List[str]]):
    # 상하좌우 비교군 상대좌표 등록
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # 단지의 수량, 집의 수량 => len():단지 수량, [0] 0번단지의 집수량
    houses = []

    # 모든 좌표를 둘러본다.
    for r in range(len(inner_map)):
        for c in range(len(inner_map[r])):
            # 현재 위치에 집이 있는 경우 진행한다.
            if inner_map[r][c] == '1':
                # 좌표 루프상 처음 발견된곳은 단지의 최초의 집이니 단지 수를 증가시킨다.
                houses.append(0)

                # 현재 위치를 스택이 기록한다.
                stack = [(r, c)]
                # 스택에 넣은 집은 0으로 처리하여 재탐색되지 않도록 한다.
                inner_map[r][c] = '0'

                # 문제점 스택에 이미 넣은 좌표를 더 깊이 파다보면 또 들어가는 구간이 있다. (해결)
                # 스택에 넣는 순간 코드를 '0'으로 바꾸어 해결하였다.
                # ----
                # 스택 => 앞으로 둘러볼 집의 좌표 리스트
                # 스택 리스트가 비어질때까지 반복한다.
                # 매 반복마다 하나의 좌표를 뽑아내어 상하좌우를 탐색한다.
                # 탐색 중 주변에 집이 별견되면 스택에 넣는다.
                while stack:
                    # 이번에 탐색할 집의 좌표를 뽑아낸다.
                    point = stack.pop()
                    # 뽑아낸 집에 대한 카운트를 증가시킨다.
                    houses[-1] += 1

                    # 상,하,좌,우 각 1번씩 4번 탐색한다.
                    for i in range(4):
                        # 상대좌표를 이용하여, 현재 집을 기준으로 상하좌우 위치를 추출한다.
                        tmp_r = point[0] + dr[i]
                        tmp_c = point[1] + dc[i]

                        # 상하좌우에 좌표를 벗어나지않은 좌표이면서, 집이 있다면, 스택에 등록한다.
                        # *등록된 집은 좌표에서 지운다. ==> 지우지 않으면 중복으로 스택에 쌓인다.
                        if n > tmp_r >= 0 and n > tmp_c >= 0 and inner_map[tmp_r][tmp_c] == '1':
                            stack.append((tmp_r, tmp_c))
                            inner_map[tmp_r][tmp_c] = '0'

    # 결과 의도에 맞게 정리하여 출력한다.
    houses.sort()
    print(len(houses))
    print('\n'.join(map(str, houses)))


# 정사각형 좌표의 가로세로 크기 입력
n = int(input())
# 빈 좌표 생성
map_ = []
# 크기에 맞게 좌표 입력
for _ in range(n):
    map_.append(list(input()))

solution(map_)
