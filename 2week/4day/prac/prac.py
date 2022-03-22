from structures import TreeNode


# 이진트리의 배열리스트를 전달 받으면, 이진트리를 구성하여 루트를 반환한다.
def make_tree_by(lst, idx):
    # 현재 idx에 해당하는 노드를 담을 변수이다.
    parent = None

    # idx가 lst에 없는 범위라면 재귀를 멈춘다.
    if idx < len(lst):
        # 리스트에 있는 노드의 값을 추출한다.
        value = lst[idx]
        # 해당 idx의 값이 없을 경우는, 완전 이진트리가 아니라는 의미이다.
        if value is None:
            return

        # 현재 idx에 대한 노드를 생성한다.
        parent = TreeNode(value)
        # 현재 노드의 자식노드들을 찾아낸다.
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

        # 현재 노드를 반환한다.
        return parent
