# https://leetcode.com/problems/odd-even-linked-list/

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


# 주어진 연결리스트에서 홀수번째, 짝수번재를 그룹화하여 홀수그룹->짝수그룹 순으로 연결한 연결리스트를 반환한다.
# 홀수 그룹 연결리스트 l1, 짝수 그룹 연결리스트 l2로 구분하여 순차적으로 그룹화한 뒤
# l1의 링크를 l2의 head(l2_head)로 연결한다. ( 공간복잡도가 1 이므로 이 방법은 안된다. )
# l1, l2 각 현재 노드를 바라보는 cur 변수를 이용하여 유기적으로 해보았다.
# l1의 head(l1_head)를 반환한다.
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 노드가 0개인 연결리스트일 경우
        if head is None:
            return None
        # 노드가 1개 일 경우
        if head.next is None:
            return head

        # 초기 필요 변수 정의
        l1_cur = head
        l2_cur = head.next
        l1_head = head  # head는 홀수번째 노드이다.
        l2_head = head.next  # head의 다음 노드는 짝수번째 노드이다.

        curNode = l2_cur.next
        count = 3
        while curNode:
            if count % 2 == 1:
                l1_cur.next = curNode
                l1_cur = curNode
                curNode = curNode.next
                l1_cur.next = l2_head
            else:
                l2_cur.next = curNode
                l2_cur = curNode
                curNode = curNode.next
            l2_cur.next = None
            count += 1

        return l1_head
