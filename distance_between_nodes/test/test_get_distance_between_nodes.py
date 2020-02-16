import unittest
from unittest import TestCase
from binarytree import Node
from main import get_distance_between_nodes


class TestDistanceBetweenNodes(TestCase):

    def test_get_distance_between_nodes(self):
        """
        To test and vaildate:
        1. The distnance between nodes
        2. Check if both nodes are  present
        3. Check if both nodes are at same level
        :return: True value
        """

        input_data_one = [7, 1]
        input_data_one_result = "Distance between node 7 and 1 is : 2"

        input_data_two = [7, 6]
        input_data_two_result = "Nodes are not at same level"

        input_data_three = [7, 10]
        input_data_three_result = "Either one of node is not present in Binary Tree"

        input_data_four = [9, 6]
        input_data_four_result = "Distance between node 9 and 6 is : 6"

        root = Node(5)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(7)
        root.left.left.left = Node(9)
        root.right.right = Node(1)
        root.right.right.left = Node(4)
        root.right.right.right = Node(6)

        distance_between_node = get_distance_between_nodes(root,
                                                           input_data_one[0],
                                                           input_data_one[1])
        self.assertEqual(distance_between_node, input_data_one_result)

        distance_between_node = get_distance_between_nodes(root,
                                                           input_data_two[0],
                                                           input_data_two[1])
        self.assertEqual(distance_between_node, input_data_two_result)

        distance_between_node = get_distance_between_nodes(root,
                                                           input_data_three[0],
                                                           input_data_three[1])
        self.assertEqual(distance_between_node, input_data_three_result)

        distance_between_node = get_distance_between_nodes(root,
                                                           input_data_four[0],
                                                           input_data_four[1])
        self.assertEqual(distance_between_node, input_data_four_result)


if __name__ == '__main__':
    unittest.main()