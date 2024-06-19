import unittest

from flatten_dublinked_lists import Node, flatten


def list_to_array(head: 'Node') -> list:
    array = []
    current = head
    while current:
        array.append(current.val)
        current = current.next
    return array

class TestFlattenMultilevelDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.head = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        child7 = Node(7)
        child8 = Node(8)
        child9 = Node(9)
        child10 = Node(10)
        
        self.head.next = node2
        node2.prev = self.head
        node2.next = node3
        node3.prev = node2

        node2.child = child7
        child7.next = child8
        child8.prev = child7
        child8.next = child9
        child9.prev = child8
        child9.child = child10

    def test_flatten(self):
        
        flattened_head = flatten(self.head)
        
        result = list_to_array(flattened_head)
        
        expected = [1, 2, 7, 8, 9, 10, 3]
        self.assertEqual(result, expected)

    def test_empty_list(self):
        """Test for empty list: """
        self.assertIsNone(flatten(None))

    def test_single_node(self):
        single_node = Node(1)
        flattened_head = flatten(single_node)
        result = list_to_array(flattened_head)
        expected = [1]
        """Test for single node: """
        self.assertEqual(result, expected)

    def test_no_children(self):
        
        head = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        
        head.next = node2
        node2.prev = head
        node2.next = node3
        node3.prev = node2
        
        flattened_head = flatten(head)
        result = list_to_array(flattened_head)
        expected = [1, 2, 3]
        """Test for no-offspring node list: """
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)