class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def print_list(self):
        values = []
        current = self.head

        while current is not None:
            values.append(current.data)
            current = current.next

        return values


if __name__ == "__main__":
    print("=== 연결 리스트 테스트 ===")

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)

    result = ll.print_list()
    print(f"리스트: {result}")
    print()

    print("=== 연결 리스트 테스트 2 ===")

    ll2 = LinkedList()
    ll2.append(10)
    ll2.append(20)
    ll2.append(30)
    ll2.append(40)

    result2 = ll2.print_list()
    print(f"리스트: {result2}")
