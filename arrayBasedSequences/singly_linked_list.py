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
    
    def remove_all(self, value):
        # Removes all nodes that contain the given value

        # First, remove matching nodes from the front
        while not self.is_empty() and self.head.data == value:
            self.delete_first()

        # If the list is now empty, stop
        if self.is_empty():
            return

        current = self.head

        # Check the rest of the list
        while current.next is not None:
            if current.next.data == value:

                # If the node being removed is the tail, update tail
                if current.next == self.tail:
                    self.tail = current

                current.next = current.next.next
                self.count -= 1

            else:
                current = current.next

    def display_reverse_nr(self):
        # Displays the list in reverse order without using recursion
        stack = []

        current = self.head

        # Push each node's data onto the stack
        while current is not None:
            stack.append(current.data)
            current = current.next

        print("None", end="")

        # Pop items from the stack to print in reverse order
        while len(stack) > 0:
            print(f" <- {stack.pop()}", end="")

        print(" <- Head")

# Test to delete specific nodes
if __name__ == "__main__":

    print("---- Build a forward list ----")
    forward_list = SinglyLinkedList()
    forward_list.build_list_forward([10, 20, 30, 40, 50])
    forward_list.display()

    print("Delete the first node:", end=" ")
    forward_list.delete_first()
    forward_list.display()

    print("Delete the last node:", end=" ")
    forward_list.delete_last()
    forward_list.display()

    print("Delete the interior node:", end=" ")
    forward_list.delete(30)
    forward_list.display()

    print()

    print("---- Build a backward list ----")
    backward_list = SinglyLinkedList()
    backward_list.build_list_backward([10, 20, 30, 40, 50])
    backward_list.display()

    print("Delete the first node:", end=" ")
    backward_list.delete_first()
    backward_list.display()

    print("Delete the last node:", end=" ")
    backward_list.delete_last()
    backward_list.display()

    print("Delete the interior node:", end=" ")
    backward_list.delete(30)
    backward_list.display()

    print()

    print("---- Non-recursive reverse print test ----")
    reverse_list = SinglyLinkedList()
    reverse_list.build_list_forward([10, 20, 30, 40, 50])
    print("Insertion order:", end=" ")
    reverse_list.display()
    print("Reverse order (non-recursive):", end=" ")
    reverse_list.display_reverse_nr()

    print()

    print("---- Remove all test ----")
    remove_list = SinglyLinkedList()
    remove_list.build_list_forward([1, 2, 4, 6, 1, 3, 6])
    remove_list.display()

    print("Removing 1 and all duplicates:", end=" ")
    remove_list.remove_all(1)
    remove_list.display()

    print("Removing 6 and all duplicates:", end=" ")
    remove_list.remove_all(6)
    remove_list.display()