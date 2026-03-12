import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node("Kopf") #Start

    def add_last(self, value):
        new_node = Node(value)
        last = self.get_last()
        last.next = new_node

    def get_last(self):
        current = self.head
        while current.next is not None:
            current = current.next
        return current

    def get_first(self):
        return self.head

    def length(self):
        count = 0
        current = self.head.next
        while current is not None:
            count += 1
            current = current.next
        return count

    def write_list(self):
        current = self.head.next
        while current is not None:
            print(current.value)
            current = current.next

    def __iter__(self):
        current = self.head.next
        while current is not None:
            yield current.value
            current = current.next

if __name__ == "__main__":
    lst = LinkedList()

    for _ in range(5):
        lst.add_last(random.randint(1, 100))

    print("Alles:")
    lst.write_list()

    print(f"Länge: {lst.length()}")
