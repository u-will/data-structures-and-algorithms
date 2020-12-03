import pytest
from tree import Node, BinaryTree, BinarySearchTree

def test_tree_structure():
    assert BinaryTree()

def test_left_and_right():
    tree_node = BinarySearchTree()
    tree_node.add(5)
    tree_node.add(8)
    tree_node.add(5)
    left = tree_node.root.left.value
    expect_left = 8
    right = tree_node.root.right.value
    expect_right = 5
    assert left == expect_left
    assert right == expect_right

def test_single_root():
    tree_node = BinarySearchTree()
    tree_node.add(14)
    actual = tree_node.root.value
    expected = 14
    assert actual == expected

def test_pre_order():
    tree_node = BinarySearchTree()
    tree_node.add(14)
    tree_node.add(27)
    tree_node.add(18)
    tree_node.add(19)
    actual = tree_node.pre_order()
    expected = [14, 218, 7, 8]
    assert actual == expected

def test_post_order():
    tree_node = BinarySearchTree()
    tree_node.add(7)
    tree_node.add(17)
    tree_node.add(8)
    tree_node.add(24)
    tree_node.add(2)
    actual = tree_node.post_order()
    expected = [2, 24, 8, 17, 7]
    assert actual == expected

def test_in_order():
    tree_node = BinarySearchTree()
    tree_node.add(8)
    tree_node.add(85)
    tree_node.add(6)
    tree_node.add(105)
    tree_node.add(101)
    tree_node.add(15)
    actual = tree_node.in_order()
    expected = [6, 8, 85, 101, 105, 15]
    assert actual == expected
