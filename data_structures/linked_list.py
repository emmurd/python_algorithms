# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        # print the value of the linked list
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return ', '.join([str(d) for d in result])

    def push(self, new_data):
        # add a new element in front of the list
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        # add a new element after the provided node

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        # add a new element at the end of the list
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def delete(self, data):
        # delete node for given data value
        prev_node = None
        current_node = self.head

        if current_node:
            if current_node.data == data:
                self.head = current_node.next
                return

        while current_node:
            if current_node.data == data:
                prev_node.next = current_node.next
                break

            prev_node = current_node
            current_node = current_node.next

    def delete_at(self, index):
        # delete node at given node index
        prev_node = None
        current_node = self.head

        if current_node:
            if index == 0:
                self.head = current_node.next
                return

        for i in range(index):
            prev_node = current_node
            current_node = current_node.next

        prev_node.next = current_node.next


    def get_count_iterative(self):
        count = 0
        current_node = self.head

        while current_node:
            current_node = current_node.next
            count += 1
        return count

    def get_count_recursive(self):
        return self._get_count_recursive(self.head)

    def _get_count_recursive(self, node):
        if not node:
            return 0

        return 1 + self._get_count_recursive(node.next)


    def get_node(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node

    def get_node_from_end(self, nth):
        length = self.get_count_recursive()
        if nth <= 0 or nth > length:
            return

        index = length - nth
        return self.get_node(index)

    def get_middle_node(self):
        # return the middle node of the list
        # if even nodes, return the second middle node

        fast_ptr = self.head
        slow_ptr = self.head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        return slow_ptr

    # def swap_nodes(self, data1, data2):
    #     # swap nodes without swapping data
    #     prev_node1 = None
    #     prev_node2 = None
    #     current_node1 = self.head
    #     current_node2 = self.head
    #
    #     while current_node1 and current_node1.data != data1:
    #         prev_node1 = current_node1
    #         current_node1 = current_node1.next
