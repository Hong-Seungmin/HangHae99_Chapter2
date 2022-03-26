# https://programmers.co.kr/learn/courses/30/lessons/49994
import collections


def solution(dirs):
    answer = 0

    # 캐릭터의 위치 보관 [x, y]
    character = [0, 0]

    # 명령에 따른 이동할 상대좌표(x,y) 설정
    move = dict()
    move["U"] = (0, 1)
    move["D"] = (0, -1)
    move["R"] = (1, 0)
    move["L"] = (-1, 0)

    # 좌표의 한계점 설정 [최소값, 최대값]
    limit_x = [-5, 5]
    limit_y = [-5, 5]

    # 지나간 좌표(엣지) 기록
    history = collections.defaultdict(bool)

    for char in dirs:
        # 이동될 위치의 좌표 계산
        moved_x = character[0] + move[char][0]
        moved_y = character[1] + move[char][1]

        # x 한계점 검사
        if moved_x < limit_x[0] or moved_x > limit_x[1]:
            # print("x좌표 범위를 벗어났습니다.")
            continue
        # y 한계점 검사
        if moved_y < limit_y[0] or moved_y > limit_y[1]:
            # print("y좌표 범위를 벗어났습니다.")
            continue

        # 정상적인 좌표범위내의 이동이라면, 방문여부를 확인 후 처리한다.
        # 방문하지 않은 엣지라면 저장한다.
        if not history[((character[0], character[1]), (moved_x, moved_y))]:
            # print(((character[0], character[1]), (moved_x, moved_y)))
            # ex. [0,0 -> 0,1] = True
            history[((character[0], character[1]), (moved_x, moved_y))] = True
            history[((moved_x, moved_y), (character[0], character[1]))] = True

        # 캐릭터의 좌표값을 바꾸어 이동시킨다.
        character[0] = moved_x
        character[1] = moved_y

    # 방문했던 경로의 카운트를 계산한다.
    for check in history.values():
        if check:
            answer += 1

    return answer // 2


print(solution("ULURRDLLU"))
