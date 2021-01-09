from tree_intersection import tree_intersection
from tree import BinaryTree, Node

def test_one_interstion():
    tree1 = BinaryTree()

    tree1.add(4)
    tree1.root.left = Node(9)
    tree1.root.right = Node(3)

    tree2 = BinaryTree()

    tree2.add(4)
    tree2.root.left = Node(32)
    tree2.root.right = Node(7)

    actual = tree_intersection(tree1, tree2)
    expect = [4]

    assert actual == expect

def test_multiple_interstion():
    tree1 = BinaryTree()

    tree1.add(4)
    tree1.root.left = Node(9)
    tree1.root.right = Node(3)
    tree1.root.left = Node(32)
    tree1.root.right = Node(3)

    tree2 = BinaryTree()

    tree2.add(4)
    tree2.root.left = Node(32)
    tree2.root.right = Node(7)
    tree2.root.left = Node(32)
    tree2.root.right = Node(3)

    actual = tree_intersection(tree1, tree2)
    expect = [4, 32, 3]

    assert actual == expect
