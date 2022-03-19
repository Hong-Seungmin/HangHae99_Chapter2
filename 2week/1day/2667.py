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
def solution(map: List[List[str]]):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    houses = []  # 단지의 수량, 집의 수량 => len():단지 수량, [0] 0번단지의 집수량

    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == '1':
                houses.append(0)

                stack = [(r, c)]

                # 문제점 스택에 이미 넣은 좌표를 더 깊이 파다보면 또 들어가는 구간이 있다.
                while stack:
                    point = stack.pop()
                    houses[-1] += 1
                    map[point[0]][point[1]] = '0'

                    for i in range(4):
                        tmp_r = point[0] + dr[i]
                        tmp_c = point[1] + dc[i]
                        if n > tmp_r >= 0 and n > tmp_c >= 0 and map[tmp_r][tmp_c] == '1':
                            stack.append((tmp_r, tmp_c))
    houses.sort()
    print(len(houses))
    print(houses)


n = int(input())
map = []
for _ in range(n):
    map.append(list(input()))

solution(map)
