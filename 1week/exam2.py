# # https://programmers.co.kr/learn/courses/30/lessons/42586
import math


#
#
# def solution(progresses, speeds):
#     answer = []
#
#     job_days = []
#
#     for i, item in enumerate(progresses):
#         days = math.ceil((100 - item) / speeds[i])
#         job_days.append(days)
#
#     # [5, 10, 1, 1, 20, 1]
#     delay = 0
#     day = 0
#     while job_days:
#         if delay == 0:
#             day = job_days.pop(0)
#             if not job_days:
#                 break
#
#         delay += 1
#         next_day = job_days[0]
#         if day <= next_day:
#             answer.append(delay)
#             delay = 0
#         else:
#             job_days.pop(0)
#
#     answer.append(delay+1)
#     return answer
#
#
# print(solution([93, 30, 55], [1, 30, 5]))


# [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]
def solution(progresses, speeds):
    answer = []
    job_days = []

    # job_days = [5, 10, 1, 1, 20, 1]
    for i, item in enumerate(progresses):
        days = math.ceil((100 - item) / speeds[i])
        job_days.append(days)

    cnt = 0 # 배포 갯수

    # 모든 잡이 끝날때까지
    while job_days:
        cnt += 1
        job = job_days.pop(0)

        # 잡이 있으면서, 다음 잡보다 더 걸리면
        while job_days and job >= job_days[0]:
            cnt += 1
            job = job_days.pop(0)

        answer.append(cnt)
        cnt = 0

    return answer


# [93, 30, 55], [1, 30, 5]
def solution(progresses, speeds):
    answer = []
    time = 0  # 작업 시간(일), 모든 작업이 동시에 진행하므로 매일 누적된다.
    count = 0  # 일일 배포 갯수

    while len(progresses) > 0:

        # 작업이 완료된것이 있다면, 배포 카운트를 올린다.
        if (progresses[0] + time * speeds[0]) >= 100:

            # 완료한것은 작업목록에서 제외
            progresses.pop(0)
            speeds.pop(0)

            # 배포 카운트 증가
            # 오늘 다른 작업물의 완료상태를 확인해야하니 time은 증가하지 않는다.
            count += 1

        # 현재 작업이 완료되지 않았다면,
        else:
            # 이전에 완료한 작업이 있으면 배포한다.
            if count > 0:
                answer.append(count)
                count = 0 # 배포하였으니 다시 카운트는 0으로 설정

            # 오늘 작업량에 대한 하루 증가
            time += 1

    answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
