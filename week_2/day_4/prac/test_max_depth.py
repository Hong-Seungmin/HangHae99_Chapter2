from collections import deque

from prac import make_tree_by


# 이진트리 배열의 최대 깊이를 구한다.
def test_max_depth(lst):
    # 주어진 배열을 이진트리로 구성하여 루트를 반환 받는다.
    # 이후 root부터 노드별로 자식을 지정할 수 있게 된다.
    root = make_tree_by(lst, 0)
    if not root:
        return 0

    # queue를 이용하여 bfs방식으로 깊이를 계산한다.
    # 루트부터 시작
    q = deque([root])
    depth = 0

    # while문은 동일 깊이에서 한번 반복한다.
    # 이후 for문에서 형제노드들을 모두 탐색하며,
    # 각각의 자식노드들을 큐에 담는다.
    # 모든 자식을 찾으면, while문이 새로 돌게되며,
    # depth가 1 증가, 자식의 자식노드를 탐색한다.
    while q:
        depth += 1
        # 형제노드를 모두 찾는다.
        for _ in range(len(q)):
            cur = q.popleft()
            # 좌우 자식이 있다면 큐에 담는다.
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth


assert test_max_depth(lst=[]) == 0
assert test_max_depth(lst=[3, 9, 20, None, None, 15, 7]) == 3
