# split_evens_odds.py
# This file contains the SplitEvensOdds class.
# It inherits from SinglyLinkedList and splits nodes into even and odd lists.

from singly_linked_list import SinglyLinkedList


class SplitEvensOdds(SinglyLinkedList):
    def split_even_odd(self):
        # Checks if the list is empty
        if self.is_empty():
            raise Exception("List is empty")

        # Creates the two new lists
        even_list = SinglyLinkedList()
        odd_list = SinglyLinkedList()

        # Starts at the head of the original list
        current = self.head

        # Clears the original list
        self.head = None
        self.tail = None
        self.count = 0

        # Goes through each node from the original list
        while current is not None:
            # Saves the next node before disconnecting current
            next_node = current.next

            # Disconnects the current node from the original chain
            current.next = None

            # If the node data is even, add it to the even list
            if current.data % 2 == 0:
                if even_list.tail is None:
                    even_list.head = current
                    even_list.tail = current
                else:
                    even_list.tail.next = current
                    even_list.tail = current

                even_list.count += 1

            # Otherwise, add it to the odd list
            else:
                if odd_list.tail is None:
                    odd_list.head = current
                    odd_list.tail = current
                else:
                    odd_list.tail.next = current
                    odd_list.tail = current

                odd_list.count += 1

            # Moves to the next saved node
            current = next_node

        # Returns both new lists
        return even_list, odd_list

if __name__ == "__main__":
    original_list = SplitEvensOdds()

    original_list.build_list_forward([1, 2, 3, 4, 5, 6, 7, 8, 15, 14, 13, 12, 11, 10, 9])

    original_list.display()

    evens_list, odds_list = original_list.split_even_odd()

    evens_list.display()
    odds_list.display()
    original_list.display()