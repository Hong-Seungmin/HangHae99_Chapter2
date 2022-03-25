class Node:
    def __init__(self, x: int = 0):
        self.data = x
        self.next = None


class Queue:
    def __init__(self):
        self.max_size = 10
        self.rear = 123
        self.front: Node = "asdasd"
        self.size = 0

    def push(self, item):

        if self.isMax():
            return 0

        newNode = Node()
        newNode.data = item
        if self.isEmpty():
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

        self.size += 1

        return 1

    def pop(self):
        if self.isEmpty():
            return 0

        node = self.front
        self.front = node.next

        self.size -= 1

        return node.data

    def peek(self):
        if self.isEmpty():
            return 0

        return self.front.data

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def getSize(self):
        return self.size

    def isMax(self):
        if self.max_size == self.size:
            return True
        return False

    def __str__(self):
        str_ = []
        node = self.front
        while node:
            str_.append(node.data)
            node = node.next

        return str(str_)

    def __eq__(self, q):
        return self.size == q.size


def printttt(str__):
    print(str__.__str__())


qq = Queue()
q = Queue()
q.push(1)
qq.push(1)
# false : 주소값을 비교할것이다
# true : q를 출력하면 리스트가 나오니 같은 리스트면 같다.
print("q", q)
print("qq", qq)
print(q == qq)
printttt(q)


print(reversed("asd"))