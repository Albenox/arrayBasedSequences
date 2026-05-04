# singly_linked_list.py
# This file contains the Node class and SinglyLinkedList class.


class Node:
    def __init__(self, data):
        # Stores the value inside the node
        self.data = data

        # Stores a reference to the next node
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        # The head points to the first node in the list
        self.head = None

        # The tail points to the last node in the list
        self.tail = None

        # The count keeps track of how many nodes are in the list
        self.count = 0

    def is_empty(self):
        # Returns True if the list has no nodes
        return self.head is None

    def display(self):
        # Displays all nodes in the list
        current = self.head

        print("Head", end="")

        while current is not None:
            print(f" -> {current.data}", end="")
            current = current.next

        print(" -> None")

    def build_list_forward(self, values):
        # Builds the list in the same order as the values given
        for value in values:
            new_node = Node(value)

            # If the list is empty, the new node becomes both head and tail
            if self.is_empty():
                self.head = new_node
                self.tail = new_node

            # Otherwise, attach the new node after the current tail
            else:
                self.tail.next = new_node
                self.tail = new_node

            self.count += 1

    def build_list_backward(self, values):
        # Builds the list in reverse order from the values given
        for value in values:
            new_node = Node(value)

            # If the list is empty, the new node becomes both head and tail
            if self.is_empty():
                self.head = new_node
                self.tail = new_node

            # Otherwise, attach the new node before the current head
            else:
                new_node.next = self.head
                self.head = new_node

            self.count += 1


# Temporary test code
if __name__ == "__main__":
    my_list = SinglyLinkedList()

    print("---- Build a forward list ----")
    my_list.build_list_forward([10, 20, 30, 40, 50])
    my_list.display()

    print("---- Build a backward list ----")
    my_list = SinglyLinkedList()
    my_list.build_list_backward([10, 20, 30, 40, 50])
    my_list.display()