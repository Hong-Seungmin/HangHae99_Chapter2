# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 주어진 두개의 정렬된 링크드리스트를 이용하여 하나의 정렬된 링크드리스트를 반환한다.
# (현재 커서 노드) (임시 보관 노드) (결과 head 노드) 3가지 변수를 활용하였다.
# 시작 시점에서 (list1과 list2의 첫 노드값을 비교)하여
# (작은 list의 노드(A)의 다음노드를 임시노드에 보관) 후
# (A노드가 시작 노드이므로 결과head 노드에 넣어준다.)
# (A의 링크를 큰 list의 노드 B로 바라보게 바꿔준다.)
# 노드 A는 이미 처리한 노드이므로 더이상 필요가 없으며,
# (노드 B를 현재 커서가 있으므로 현재 노드에 보관하여 초기화를 마친다.)
# 이후 반복적으로 (현재 노드)와 (임시 노드)를 비교하며 진행한다.
# while (현재노드와 임시노드가 둘다 None일때까지)
# if (임시노드가 None이라면)
# ---- (현재노드를 현재노드의 다음노드로 바꿔준다.) ==> 그냥 break해도 된다.
# elif (현재노드의 다음 노드가 None이라면)
# ----(현재노드의 링크를 임시노드로 바라보게 한다.)
# ----(현재노드를 임시노드로 바꿔준다.)
# ----(임시노드는 None으로 바꿔준다.)
# elif (현재노드가 더 작은 값이라면)
# ----(현재노드를 다음 노드로 변경한다.)
# else (임시노드가 더 작은 값이라면)
# ----(현재노드의 다음 노드를 별도 보관한 후) -> 스와핑 변수
# ----(현재노드의 링크를 임시노드로 바라보게 변경한다.)
# ----(이후 현재노드에 임시노드를 넣고)
# ----(임시노드에 별도 보관한 노드를 넣는다.)
# return 결과 head 노드
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curNode = None
        temporaryNode = None
        resultHeadNode = None

        # list1과 list2 중 None이 존재할 경우
        # list1가 None 이면 list2를
        # list2가 None 이면 list1을
        # 둘다 None 이면 None을 curNode에 넣어준다.
        if list1 is None or list2 is None:
            curNode = list1 if list1 else list2 if list2 else None
        # 두 노드 모두 존재할 경우
        # 두 노드 중 작은 노드를 현재 노드로 설정하고,
        # 큰 노드는 임시보관 노드로 설정한다.
        else:
            # 아래 라인은 [too many values to unpack] ValueError가 뜨는데 왜 뜨는지 아직 모르겠다.
            # curNode, temporaryNode = list1, list2 if list1.val < list2.val else list2, list1
            # 그래서 일반적으로 바꿨다.
            if list1.val <= list2.val:
                curNode = list1
                temporaryNode = list2
            else:
                curNode = list2
                temporaryNode = list1

        # 리턴할 head노드에 현재 커서를 넣어 시작점을 알려준다.
        resultHeadNode = curNode

        # 현재노드와 임시노드를 반복적으로 탐색하여 값을 비교 후 적절하게 링크를 연결해준다.
        # 두 노드가 모두 None이 될때까지 반복한다.
        while curNode or temporaryNode:
            # 임시노드가 None이라면,
            # 더이상 변경할 것이 없으므로 반복을 마친다.
            if temporaryNode is None:
                break
            # 현재노드의 다음노드가 None이라면,
            # 현재노드는 더이상 진행할 것이 없으므로
            # 현재노드의 링크를 임시노드로 설정하여 반복을 마친다.
            elif curNode.next is None:
                curNode.next = temporaryNode
                break
            # 현재노드와 다음노드가 임시노드보다 작거나 같은 값이라면,
            # 현재노드를 다음 노드로 바꿔준다.
            elif curNode.val < temporaryNode.val and curNode.next.val < temporaryNode.val:
                curNode = curNode.next

            # 임시노드가 더 작은 값이라면,
            # "현재노드의 다음노드"와 "임시노드"를 스왑해야한다.
            # 스왑을 위해 임시변수에 "현재노드의 다음노드"를 보관하고,
            # 현재노드와 임시노드를 바꿔준다.
            else:
                tmp = curNode.next
                curNode.next = temporaryNode
                curNode = temporaryNode
                temporaryNode = tmp

        return resultHeadNode
