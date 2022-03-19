# https://leetcode.com/problems/reconstruct-itinerary/
import collections
from typing import List


# 주어진 티켓쌍[from,to]를 가지고 모든 티켓을 소모하여 여행을 갈 수 있는 구조를 반환한다.
# 출발지는 "JFK"에서 출발한다.
# 동시에 갈수있는곳이 복수일 경우 사전순으로 이동한다.
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        pass

    # ############################################
    # ####### 1차 실패, 이동중 더이상 갈곳이 없고, 후진도 못하는 곳은 마지막에 들려야한다.
    #
    #  # 여행하면서 거친 공항을 등록한다.
    #  answer = []
    #
    #  # 티켓들을 (dict[from] = to, ...) 로 정리한다.
    #  tickets_dict = collections.defaultdict(list)
    #  for ticket in tickets:
    #      ticket_from = ticket[0]
    #      ticket_to = ticket[1]
    #      tickets_dict[ticket_from].append(ticket_to)
    #
    #  # 한곳에서 여러곳을 갈 수 있다면, 정렬하여 사전순으로 우선권을 부여한다.
    #  for ticket_from in tickets_dict.keys():
    #      tickets_dict[ticket_from].sort(reverse=True)
    #
    #  # 큐를 생성하여 여행대기열을 만든다.
    #  # 첫 여행지는 "JFK" 이므로 초기등록한다.
    #  queue = ["JFK"]
    #
    #  # 대기열이 사라질때까지 여행을 시킨다.
    #  # 대기열이 없다면, 여행을 종료한다.
    #  while queue:
    #      # 출발지를 뽑아낸다.
    #      src = queue.pop()
    #      # 출발지를 결과용으로 등록한다.
    #      answer.append(src)
    #
    #      # 다음 티켓이 있다면,
    #      # 목적지를 대기열에 넣는다.
    #      if tickets_dict[src]:
    #          queue.append(tickets_dict[src].pop())
    #
    #  return answer
    #  ###########################################


sol = Solution()
assert sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) \
       == ["JFK", "MUC", "LHR", "SFO", "SJC"], "오답"
print("테스트1 통과")
assert sol.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) \
       == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"], "오답"
print("테스트2 통과")
assert sol.findItinerary(
    [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]) \
       == ["JFK", "NRT", "JFK", "KUL"], "오답"
print("테스트3 통과")
