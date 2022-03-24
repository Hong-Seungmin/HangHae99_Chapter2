# 선행학습으로 힙을 구현해보고자 한다.
# 구현한 힙을 이용하여, 힙정렬 문제에 사용할 수 있게 만들어 보는것이 목표이다.
import random


class Heap:
    """
    reverse = False : [최소힙:True],[최대힙:False]을 선택한다.
    """

    # 객체 생성시 바로 아이템을 넣을 수 있고,
    # reverse를 이용하여 최소,최대힙을 선택할 수 있다.
    def __init__(self, reverse=True):
        self.list = list()
        self.reverse = reverse
        self._size = 0

    # 상황에 따라 트리를 재구성한다.
    # 삽입, 삭제 연산이 일어날때
    # 노드를 재구성하여 힙의 규칙을 유지하게 만든다.
    def heapify(self, index):
        # 자식들의 인덱스를 추출한다.
        child_left_index = self.get_child_left_index(index)
        child_right_index = self.get_child_right_index(index)
        swap_tmp_index = index

        # 왼쪽 자식과 부모의 값을 비교한다.
        # 자식 index가 last_index보다 더 크다는 것은 자식이 없는 것이다.
        if child_left_index <= self.get_last_index():
            if self.list[swap_tmp_index] > self.list[child_left_index]:
                swap_tmp_index = child_left_index

        # 오른쪽 자식과 부모의 값을 비교한다.
        # 왼쪽자식이 더 작은 상황에서 오른쪽이 더 작다면 오른쪽으로 교체한다.
        if child_right_index <= self.get_last_index():
            if self.list[swap_tmp_index] > self.list[child_right_index]:
                swap_tmp_index = child_right_index

        # 부모의 값이 자식보다 크다면, 스왑 후 하위 노드들도 정리한다.
        if swap_tmp_index != index:
            self.item_swap(index, swap_tmp_index)
            self.heapify(swap_tmp_index)

    # 1. 힙의 put 연산은 list의 마지막에 새로운 노드를 삽입,
    # 2. 이후 부모노드부터 루트노드까지 힙을 재정리한다.
    def put(self, item):
        # reverse 옵션에 따른 값으로 바꿔준다.
        item = self.get_reverse_value(item)

        # 노드를 추가한다.
        self.list.append(item)
        self._size += 1

        # 추가한 노드는 last_index를 가지며, 부모 노드부터 루트까지 재정리한다.
        last_index = self.get_last_index()
        parent_index = self.get_parent_index(last_index)
        for index in range(parent_index, -1, -1):
            self.heapify(index)

    # 1. 힙의 pop 연산은 루트노드를 빼네고,
    # 2. 마지막 노드를 루트자리로 이동시킨 후
    # 3. 루트부터 리프노드까지 트리를 재정리한다.
    def pop(self):
        if self.isEmpty():
            return None

        # 루트와 마지막 인덱스를 뽑아낸다.
        root_index = self.get_root_index()
        last_index = self.get_last_index()

        # 루트와 마지막 노드의 위치를 맞바꾼다.
        # 스왑을 먼저하는 이유는 파이썬의 list.pop 은 O(1) 이기 때문이다.
        self.item_swap(root_index, last_index)

        # 마지막 노드(실제로는 루트노드)를 뽑아내고 힙 사이즈를 1 감소시킨다.
        pop_value = self.list.pop()
        self._size -= 1

        # 힙 트리를 재정리 한다.
        self.heapify(root_index)

        # 뽑아낸 루트노드를 반환한다.
        return self.get_reverse_value(pop_value)

    # peek 연산은 루트 노드의 값을 반환한다.
    def peek(self):
        if self.isEmpty():
            return None

        return self.list[self.get_root_index()]

    def get_last_index(self):
        return self._size - 1

    def isEmpty(self):
        return self._size == 0

    def get_root_index(self):
        return 0

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def get_child_left_index(self, parent_index):
        return parent_index * 2 + 1

    def get_child_right_index(self, parent_index):
        return parent_index * 2 + 2

    def item_swap(self, index_one, index_two):
        self.list[index_one], self.list[index_two] = self.list[index_two], self.list[index_one]

    def get_reverse_value(self, item):
        return item if self.reverse else (-1) * item

    def __str__(self):
        return list(map(self.get_reverse_value, self.list)).__str__()


if __name__ == "__main__":

    heap = Heap(reverse=False)
    for _ in range(50):
        heap.put(random.randrange(0, 50))
    print(heap.__str__())
    for _ in range(50):
        print(heap.pop())
