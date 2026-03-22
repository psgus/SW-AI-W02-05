class Node:
    """연결 리스트의 노드"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """단순 연결 리스트"""
    def __init__(self):
        self.head = None


    def append(self, data):
        """리스트 끝에 노드 추가"""
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current = self.head

        while current.next != None:
            current = current.next

        current.next = new_node


    def print_list(self):
        """리스트의 모든 값 출력"""
        values = []

        current = self.head

        while current:
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


    print("=== 연결 리스트 테스트 2 ===")
vv
    ll2 = LinkedList()
    ll2.append(10)
    ll2.append(20)
    ll2.append(30)
    ll2.append(40)

    result2 = ll2.print_list()
    print(f"리스트: {result2}")