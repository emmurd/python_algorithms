import unittest

from data_structures.linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)
        self.list.append('a')

    def test_push(self):
        self.list = LinkedList()
        self.list.push(1)
        self.list.push(2)
        self.list.push('a')

        assert str(self.list) == 'a, 2, 1'

    def test_insert_after(self):
        self.list = LinkedList()
        self.list.push(1)
        self.list.push([1,2])
        self.list.push(3)

        node = self.list.head.next
        self.list.insert_after(node, 'a')

        assert str(self.list) == '3, [1, 2], a, 1'

    def test_append(self):
        self.list = LinkedList()
        self.list.append(1)
        self.list.append(2)
        self.list.append('a')

        assert str(self.list) == '1, 2, a'


    def test_delete(self):
        self.list.delete(2)
        assert str(self.list) == '1, 3, a'

        self.list.delete(1)
        assert str(self.list) == '3, a'

    def test_delete_at(self):
        self.list.delete_at(1)
        assert str(self.list) == '1, 3, a'

        self.list.delete_at(0)
        assert str(self.list) == '3, a'

    def test_get_count_iterative(self):
        assert self.list.get_count_iterative() == 4

    def test_get_count_recursive(self):
        assert self.list.get_count_recursive() == 4

    def test_get_node(self):
        assert self.list.get_node(0).data == 1
        assert self.list.get_node(1).data == 2
        assert self.list.get_node(2).data == 3

    def test_get_node_from_end(self):
        assert self.list.get_node_from_end(1).data == 'a'
        assert self.list.get_node_from_end(2).data == 3
        assert self.list.get_node_from_end(0) == None
        assert self.list.get_node_from_end(5) == None

    def test_get_middle_node(self):
        assert self.list.get_middle_node().data == 3

        self.list.append(['a', 2, None])
        assert self.list.get_middle_node().data == 3
