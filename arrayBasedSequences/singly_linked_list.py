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

    def delete_first(self):
        # Deletes the first node in the list
        if self.is_empty():
            raise Exception("List is empty")

        self.head = self.head.next
        self.count -= 1

        # If list becomes empty, update tail
        if self.head is None:
            self.tail = None


    def delete_last(self):
        # Deletes the last node in the list
        if self.is_empty():
            raise Exception("List is empty")

        # If only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            current = self.head

            # Traverse to the second-to-last node
            while current.next != self.tail:
                current = current.next

            current.next = None
            self.tail = current

        self.count -= 1


    def delete(self, value):
        # Deletes the first occurrence of a value (interior delete)
        if self.is_empty():
            raise Exception("List is empty")

        # If deleting the first node
        if self.head.data == value:
            self.delete_first()
            return

        current = self.head

        # Find the node before the one to delete
        while current.next is not None and current.next.data != value:
            current = current.next

        # If value not found
        if current.next is None:
            return

        # If deleting the last node
        if current.next == self.tail:
            self.delete_last()
        else:
            current.next = current.next.next
            self.count -= 1

# Test to delete specific nodes
if __name__ == "__main__":
    my_list = SinglyLinkedList()

    print("---- Build a forward list ----")
    my_list.build_list_forward([10, 20, 30, 40, 50])
    my_list.display()

    print("Delete the first node:")
    my_list.delete_first()
    my_list.display()

    print("Delete the last node:")
    my_list.delete_last()
    my_list.display()

    print("Delete an interior node (30):")
    my_list.delete(30)
    my_list.display()