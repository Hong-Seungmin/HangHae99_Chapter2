# https://leetcode.com/problems/reverse-linked-list/

# Given the head of a singly linked list, reverse the list, and return the reversed list.

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


# 주어진 링크드리스트를 역순으로 바꾸어 반환한다.
# 3개의 변수를 활용하여, (이전노드:preNode) (현재노드:curNode) (이후노드:postNode) 를 선정하여,
# 전후 노드의 next 링크를 뒤바꾼다.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 빈 리스트일 경우 None 처리
        if not head:
            return None

        # 헤드(첫번째 노드)를 이전 노드로 설정한다.
        # 반복문 시작 노드는 2번째 노드이다.
        preNode = head
        curNode = head.next  # 현재노드는 2번째 노드이다.

        # 역순이므로 첫번째 노드의 next는 None 처리한다. (결과적으로 마지막 노드가 됨)
        preNode.next = None

        # 현재노드를 한칸씩 진행하면서 None일때까지 반복한다.
        while curNode:

            # 다음노드를 정해준 뒤 현재노드의 next를 이전노드로 방향을 바꿔준다.
            postNode = curNode.next
            curNode.next = preNode

            # 이전노드와 현재노드를 앞으로 한단계 이동한다.
            #    - 이전노드는 더이상 필요가 없으므로 현재노드를 이전노드로 바꿔준다.
            #    - 현재노드도 필요가 없으므로 이후노드를 현재노드로 바꿔준다.
            preNode = curNode
            curNode = postNode

        # curNode는 None이므로 curNode 이전 단계인 preNode가 마지막 노드이다. (결과적으로 시작 노드)
        return preNode
