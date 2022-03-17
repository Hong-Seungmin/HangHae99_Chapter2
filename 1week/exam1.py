# https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

# 한번에 10kg 까지만 지나갈 수 있는 다리를 트럭들이 지나가야하는 총 시간은 얼마인가?
# bridge_length : 다리의 길이, 다리의 칸 수
# weight : 다리가 버틸 수 있는 무게 , weight 이상의 무게는 지나갈 수 없다.
# truck_weights : 각 트럭의 무게
import collections


def solution(bridge_length, weight, truck_weights):
    answer = 0

    waiting = truck_weights[:]  # 대기 중인 트럭
    moving = []  # 지나가는 중인 트럭
    finish = []  # 다리를 건넌 트럭
    count = []  # 각 차량의 건너는 시간 표시

    while len(finish) < len(truck_weights):  # 모든 트럭이 통과할때까지
        answer += 1

        # 대기 중인 차량의 건널 여부 판단 후 처리
        if waiting:
            waiting_front_truck = waiting[0]
            # 다리를 건너는 차량의 총 무게와 가장 앞 대기차량의 무게가 다리 부하를 넘지 않으면 이동시킨다.
            if sum(moving) + waiting_front_truck <= weight:
                # print('moving', waiting[0])
                moving.append(waiting.pop(0))
                count.append(1)

        # 이동 중인 차량의 통과 여부 확인
        for i, k in enumerate(moving):
            if count[i] == bridge_length:
                # print('finish', k)
                finish.append(k)
                moving.pop(i)
                count.pop(i)
            else:
                count[i] += 1

    return answer


# 5, 10, [7, 4, 5, 6]
def solution(bridge_length, weight, truck_weights):
    answer = 0

    # [7,0,0 ,0 ,0]
    bridge = collections.deque([0] * bridge_length)

    while bridge:
        answer += 1
        bridge.popleft() # ['0',]
        if truck_weights:  # [7, 4, 5, 6]
            if sum(bridge) + truck_weights[0] <= weight:
                # [0, 7] , [4, 5, 6]
                bridge.append(truck_weights.pop(0)) # [6,]
            else:
                # [7, 0]
                bridge.append(0) #[7,0]
    return answer

'''
<<<-----
end [0,0,0,0,0,0] start
'''

#
# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
