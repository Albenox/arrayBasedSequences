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