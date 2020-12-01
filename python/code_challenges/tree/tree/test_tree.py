import pytest
from tree import Node, BinaryTree, BinarySearchTree

def test_tree_structure():
    assert BinaryTree()

def test_left_and_right():
    tree_stuff = BinarySearchTree()
    tree_stuff.add(3)
    tree_stuff.add(2)
    tree_stuff.add(4)
    left = tree_stuff.root.left.value
    expect_left = 2
    right = tree_stuff.root.right.value
    expect_right = 4
    assert left == expect_left
    assert right == expect_right

def test_single_root():
    tree_stuff = BinarySearchTree()
    tree_stuff.add(2)
    actual = tree_stuff.root.value
    expected = 2
    assert actual == expected

def test_pre_order():
    tree_stuff = BinarySearchTree()
    tree_stuff.add(5)
    tree_stuff.add(6)
    tree_stuff.add(7)
    tree_stuff.add(8)
    actual = tree_stuff.pre_order()
    expected = [5, 6, 7, 8]
    assert actual == expected

def test_post_order():
    tree_stuff = BinarySearchTree()
    tree_stuff.add(9)
    tree_stuff.add(19)
    tree_stuff.add(11)
    tree_stuff.add(7)
    tree_stuff.add(8)
    actual = tree_stuff.post_order()
    expected = [8, 7, 11, 19, 9]
    assert actual == expected

def test_in_order():
    tree_stuff = BinarySearchTree()
    tree_stuff.add(90)
    tree_stuff.add(80)
    tree_stuff.add(85)
    tree_stuff.add(60)
    tree_stuff.add(95)
    tree_stuff.add(91)
    tree_stuff.add(101)
    actual = tree_stuff.in_order()
    expected = [60, 80, 85, 90, 91, 95, 101]
    assert actual == expected
