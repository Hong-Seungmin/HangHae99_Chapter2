# https://www.acmicpc.net/problem/2468

# 입력한 지도에서 내리는 비의 양에 따라 안전지대가 최대한 생길 수 있는 개수는 얼마인가?
# 입력 : 첫째 줄 = 좌표의 크기 (정사각형 N)
#       둘째 줄부터 = 각 좌표의 높이
# 5
# 6 8 2 6 2
# 3 2 3 4 6
# 6 7 3 3 2
# 7 2 5 3 6
# 8 9 5 2 7
import copy
from pprint import pprint

# 문제 제약사항 중 있을 수 없는 값을 식별자로 선택
CHECKED = 101

# 입력사항 입력
N = int(input())
map_origin = []
for i in range(N):
    map_origin.append(list(map(int, input().split())))

# 좌표 중 가장 높은 높이 보관
max_height = max(map(max, map_origin))

# 상하좌우 상대좌표 정의
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 1~최대높이까지 돌면서,
# result에는 가장 많은 구역 수 저장
# count에는 높이별 구역 수 저장
result = 0
count = 0

# range범위는 입력된 높이 중 가장 낮은곳에서 가장 높은곳으로 하는게 효율적이다.
# 높이마다 x,y모두 +1씩 늘리며 전부 탐색
for limit in range(1, max_height + 1):
    # 안전높이 마다 초기화
    count = 0
    map_tmp = copy.deepcopy(map_origin)

    # 모든 좌표 탐색
    for x in range(N):
        for y in range(N):
            # 탐색할 필요없는 곳은 패스 ( 침수구역 or 이미 탐색한 구역 )
            if map_tmp[x][y] == CHECKED or map_tmp[x][y] < limit:
                continue

            # 구역 카운트 증가 ( 한번 들어오면 주변 모든 구역을 탐색한다. )
            count += 1

            # 탐색 시작 좌표 등록
            stack = [(x, y)]
            map_tmp[x][y] = CHECKED

            # 주변부를 탐색하며 stack에 넣으면서 인접구역 모두 탐색
            while stack:
                point = stack.pop()

                # 상하좌우 탐색
                for i in range(4):
                    # 상대좌표를 이용하여 절대좌표 획득
                    tmp_x = point[0] + dx[i]
                    tmp_y = point[1] + dy[i]

                    # 맵을 벗어나거나, 이미 탐색한 구역이거나, 침수구역일 경우 무시
                    if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= N or map_tmp[tmp_x][tmp_y] == CHECKED or \
                            map_tmp[tmp_x][tmp_y] < limit:
                        continue
                    # 안전구역이라면 stack에 등록, 안전구역 확인 처리
                    else:
                        stack.append((tmp_x, tmp_y))
                        map_tmp[tmp_x][tmp_y] = CHECKED

    # 침수높이마다 계산한 count와 기존 result 중 높은 값을 보관
    result = max(count, result)

print(result)
