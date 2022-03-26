# https://leetcode.com/problems/palindrome-linked-list/

# Given the head of a singly linked list, return true if it is a palindrome.

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


# 주어진 링크드리스트가 팰린드롬 문자열인지 확인하여 반환한다.
# 먼저 리스트를 끝까지 탐색하여,
# (리스트 길이)를 구한다.
# 다음으로 길이의 반만큼 이동하여,
# 중간 노드부터 마지막 노드까지 탐색하며,
# (링크 방향)을 역전, (마지막 노드)를 구한다.
# 마지막으로 (head부터 중간까지),
# 그리고 (마지막 노드부터 중간까지)
# (각 노드의 값이 같은가 비교하며 중간으로 탐색)한다.
# (len(list) / 2 만큼 이동)하며 (결과를 반환)한다.
# 반환값 : len(list) / 2 만큼 이동이 되었다면 true,
#        중간에 비교값이 다르다면 false
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        listCount = 0

        # 리스트 길이를 구하기 위해 끝까지 탐색한다.
        while node:
            listCount += 1

            node = node.next

        # 구한 길이를 기준으로 중간 노드까지 이동한다.
        i = 0
        node = head

        # 짝수/홀수 길이 전부다 탐색
        # 홀수 길이는 정 중앙 노드까지 탐색하여야 한다.
        # ex) listCount가 5일 경우 반값은 2.5이며, 2번 탐색하면된다. 중간값 : 3번째
        # ex) listCount가 4일 경우 반값은 2이며, 2번 탐색한다. 중간값 : 3번째
        while i < int(listCount / 2):
            node = node.next
            i += 1

        # 중간에서부터 마지막 노드까지 링크를 반전하며 진행
        preNode = None
        while node:
            tmp = node.next
            node.next = preNode
            preNode = node
            node = tmp

        lastNode = preNode  # node는 Node을 가지므로, preNode가 마지막 노드이다.
        firstNode = head  # head는 시작 노드이다.
        i = 0
        # 짝수 길이는 전부다 탐색
        # 홀수 길이는 정 중앙 노드는 탐색하지 않아도 된다.
        # ex) listCount가 5일 경우 반값은 2.5이며, 2번만 탐색하면된다.
        # ex) listCount가 4일 경우 반값은 2이므로 소수점을 버림하여 홀수짝수 모두 2번 돌게하였다.
        while i < int(listCount / 2):  # firstNode와 lastNode를 길이의 반만큼 반복하여 탐색한다.

            # 각 노드의 값을 비교하여, 틀리다면 False를 반환한다. 팰린드롬이 아니다.
            if firstNode.val != lastNode.val:
                return False
            firstNode = firstNode.next
            lastNode = lastNode.next
            i += 1

        # 반복문을 통과하였다면, 가운데를 기준으로 양옆이 같다는 것이므로 팰린드롬이다.
        return True

