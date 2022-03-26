# # https://programmers.co.kr/learn/courses/30/lessons/42586
import math


# 모범답안을 보고 새로 작성

# 모든 작업은 동시에 진행된다.
# progresses는 완성도를 의미하며, 100이되면 배포할 수 있는 상태가 된다.
# sppeds는 하루에 할 수 있는 완성도이다.
# 각 배포의 우선순위는 앞에서부터 뒤로갈수록 낮아진다.
# 즉, 앞 작업이 덜 끝났으면 뒷 작업은 배포를 할 수 없다.
# 각 리스트의 동일 인덱스끼리 매칭된다.
# answer에는 배포를 할 수 있는 날을 기준으로 그날 몇개의 작업을 배포하였는지 보관한다.

# 예) [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]
#      ==> [1, 3, 2]  ## 작업일 상관없이 배포 순서 기준 [1개 배포, 3개 배포, 2개 배포]
def solution(progresses, speeds):
    answer = []
    day = 0  # 작업에 걸린 기간
    cnt = 0  # 한번에 배포할 수 있는 배포 카운트

    while progresses:
        # day += 1  # 하루에 n개의 작업을 완성할 수 있으니, 여기서 하루를 넘기면 안된다.

        # 완성도가 100이 넘으면 배포 카운트를 증가시킨다.
        if progresses[0] + (day * speeds[0]) >= 100:
            # 완성한 작업물 배포 준비 (배포 카운트 증가)
            cnt += 1

            # 완성된 작업을 목록에서 제거한다.
            progresses.pop(0)
            speeds.pop(0)
        else:
            # 이전 작업물에 대해서 배포 준비가 끝났다면 배포한다.
            if cnt > 0:  # 배포할것이 있다면,
                answer.append(cnt)  # 배포할 작업 갯수를 넣는다.
                cnt = 0  # 배포 등록하였으니, 다음 배포 카운트를 준비한다.
            day += 1  # 미완성된 (우선 작업)이 있다면, 하루를 넘긴다.

    # 마지막 작업이 완료되면, answer.append(cnt)를 안하고 반복문이 종료되니,
    # 마지막 배포에 대해서 수동으로 등록해준다.
    answer.append(cnt)
    return answer


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
# def solution(progresses, speeds):
#     answer = []
#     job_days = []
#
#     # job_days = [5, 10, 1, 1, 20, 1]
#     for i, item in enumerate(progresses):
#         days = math.ceil((100 - item) / speeds[i])
#         job_days.append(days)
#
#     cnt = 0 # 배포 갯수
#
#     # 모든 잡이 끝날때까지
#     while job_days:
#         cnt += 1
#         job = job_days.pop(0)
#
#         # 잡이 있으면서, 다음 잡보다 더 걸리면
#         while job_days and job >= job_days[0]:
#             cnt += 1
#             job = job_days.pop(0)
#
#         answer.append(cnt)
#         cnt = 0
#
#     return answer
#
#
# # [93, 30, 55], [1, 30, 5]
# def solution(progresses, speeds):
#     answer = []
#     time = 0  # 작업 시간(일), 모든 작업이 동시에 진행하므로 매일 누적된다.
#     count = 0  # 일일 배포 갯수
#
#     while len(progresses) > 0:
#
#         # 작업이 완료된것이 있다면, 배포 카운트를 올린다.
#         if (progresses[0] + time * speeds[0]) >= 100:
#
#             # 완료한것은 작업목록에서 제외
#             progresses.pop(0)
#             speeds.pop(0)
#
#             # 배포 카운트 증가
#             # 오늘 다른 작업물의 완료상태를 확인해야하니 time은 증가하지 않는다.
#             count += 1
#
#         # 현재 작업이 완료되지 않았다면,
#         else:
#             # 이전에 완료한 작업이 있으면 배포한다.
#             if count > 0:
#                 answer.append(count)
#                 count = 0 # 배포하였으니 다시 카운트는 0으로 설정
#
#             # 오늘 작업량에 대한 하루 증가
#             time += 1
#
#     answer.append(count)
#     return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
