from binarytree import Node


def get_distance_between_nodes(b_tree, node_one, node_two):
    """
     Takes a Tree and two Nodes as input and returns Distance Between them,
     if both are present and at same level
    :param Tree: Binary Tree as input
    :param node_one: Node 1 as an input
    :param node_two: Node 2 as an input
    :return: Distance between two node
    """

    list_of_nodes_by_level = b_tree.levels
    list_repr_of_btree = b_tree.values

    if node_one and node_two in list_repr_of_btree:
        for nodes in list_of_nodes_by_level:
            str_repr_of_nodes = ''.join([n for n in str(nodes) if n.isdigit()])
            if str(node_one) in str_repr_of_nodes and str(node_two) in str_repr_of_nodes:
                node_one_index = list_repr_of_btree.index(node_one)
                node_two_index = list_repr_of_btree.index(node_two)
                distance_between_nodes = abs(node_one_index-node_two_index)-1
                return "Distance between node {} and {} is : {}".format(node_one,
                                                                        node_two,
                                                                        distance_between_nodes)
        return "Nodes are not at same level"
    return "Either one of node is not present in Binary Tree"


if __name__ == '__main__':
    ROOT = Node(5)
    ROOT.left = Node(2)
    ROOT.right = Node(3)
    ROOT.left.left = Node(7)
    ROOT.left.left.left = Node(9)
    ROOT.right.right = Node(1)
    ROOT.right.right.left = Node(4)
    ROOT.right.right.right = Node(6)

    NODE_1 = 7
    NODE_2 = 1

    DISTANCE_BETWEEN_NODE = get_distance_between_nodes(ROOT, NODE_1, NODE_2)
    print(DISTANCE_BETWEEN_NODE)
