# https://leetcode.com/problems/course-schedule/
import collections
from typing import List


# 해당과목에 선수과목이 있다면, 선수과목을 수료하고 해당과목을 수료할 수 있다.
# [1,0] 이 주어진다면, 1을 배우기 위해선 0을 수료하여야 한다.
# 주어진 과목리스트(prerequisites)를 조사하여, 모든과목을 수료할 수 있는가 판별한다.
# numCourses는 모든 과목의 수를 나타낸다.
class Solution:
    # 순환그래프를 찾는 문제이다.
    # 순환그래프가 구성되었다면, false를
    # 순환그래프가 아니라면, true를 반환한다.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_dict = collections.defaultdict(list)

        for course in prerequisites:
            courses_dict[course[0]].append(course[1]) \
 \
        # 힌트를 보고 작성하였다. DFS 이다.

        # 순환그래프를 탐지하기위한 traced이다.
        # traced는 현재 진행중인 노드들을 담고, 처리완료된 노드는 다시 꺼낸다.
        # 즉, 탐지중 traced에 들어있는 자식노드가 나오면 순환그래프가 된다.
        traced = set()
        # 처리완료한 모든 노드를 담는다.
        visited = set()

        # 각 노드별로 dfs방식으로 순환그래프 여부를 판단한다.
        def dfs(i) -> bool:
            # 현재 진행중인 노드에 존재한다면 False
            if i in traced:
                return False
            # 이미 완료한곳이면, 중복으로 하지 않는다.
            if i in visited:
                return True

            # 현재 진행리스트에 노드를 등록한다.
            traced.add(i)

            # 자식 노드들을 재귀적으로 탐색한다.
            for course in courses_dict[i]:
                # 자식노드가 순환이라면 False를 반환한다.
                if not dfs(course):
                    return False
            # 모든 자식노드가 순환이 안된다면,
            # 이 노드 밑으로는 순환이 없으므로 진행을 완료한다.
            traced.remove(i)
            visited.add(i)

            return True

        # 각 노드마다 서브 그래프가 존재하므로,
        # 모든 노드를 기준으로 탐색한다.
        for x in list(courses_dict):
            if not dfs(x):
                return False

        return True

        # ########################################
        # ####### 실패 안, 중간노드를 완료처리하지 못하겠다.
        # ####### bfs방식으로 이미 지나간 노드 확인이 안된다.
        # ####### 별도의 지나간노드를 추적하는 공간이 필요하다.
        # for i in list(courses_dict.keys()):  # 테스트 케이스에서 0부터 시작안하는 노드가 있어서 키값을 기준으로 하였다.
        #     # for i in range(numCourses):
        #     visited_course = set()
        #     success_course = set()
        #     queue = collections.deque([i])
        #
        #     while queue:
        #         course = queue.popleft()
        #         if course in success_course:
        #             continue
        #         if course in visited_course:
        #             return False
        #         else:
        #             visited_course.add(course)
        #             if not courses_dict[course]:
        #                 success_course.add(course)
        #             else:
        #                 for sub_course in courses_dict[course]:
        #                     if sub_course not in success_course:
        #                         queue.append(sub_course)
        #
        # return True
        # ###########################################


sol = Solution()
assert sol.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]) is True
print("테스트1 완료")
assert sol.canFinish(5, [[0, 1], [1, 2], [1, 3], [2, 4]]) is True
print("테스트2 완료")
assert sol.canFinish(5, [[0, 1], [1, 2], [1, 3], [2, 4], [4, 3]]) is True
print("테스트3 완료")
assert sol.canFinish(4, [[0, 1], [1, 2], [2, 3], [3, 1]]) is False
print("테스트4 완료")
assert sol.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]) is True
print("테스트5 완료")
# asd = [1, 2, 3]
# zxc = [4, 5, 6]
#
# asd.extend(zxc)
# asd.append(zxc)
#
# print(asd)
