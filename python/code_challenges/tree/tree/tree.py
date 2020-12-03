from invalid_operation_error import InvalidOperationError
from node import Node
class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

class Queue:
    """
    Queue data structure implementation
    Note: helps to remember that the "rear" is like the "head" of a LinkedList
    and the "front" node will always have a next of None
    """
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, value):
        node = Node(value)
        if self.rear:
            self.rear.next = node
        self.rear = node
        self.front = self.front or self.rear
    def dequeue(self):
        if not self.front:
            raise InvalidOperationError("Method not allowed on empty collection")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value
    def peek(self):
        if not self.front:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value
    def is_empty(self):
        return self.front == None
class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        # root, left, right
        values = []
        def walk(root):
            if not root:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)
        walk(self.root)
        return values

    def in_order(self):
        # left, root, right
        values = []
        def walk(root):
            if not root:
                return
            walk(root.left)
            values.append(root.value)
            walk(root.right)
        walk(self.root)
        return values

    def post_order(self):
        # left, right, root
        values = []
        def walk(position):
            if not position:
                return
            walk(position.left)
            walk(position.right)
            values.append(position.value)
        walk(self.root)
        return values

    def breath_frist(self):
        if not self.root:
            raise Exception ('this tree is empty')
        value = []
        q = Queue()
        q.enqueue(self.root)

        while not is_empty():
            val = q.dequeue()
            if val.left:
                q.enqueue(val.left)
            if val.right:
                q.enqueue(val.right)
            value.append(val)
        return value





class BinarySearchTree(BinaryTree):

    def contains(self, value):
        if value not in self.pre_order():
            return False
        else:
            return True
    def add(self, value):
        new_n = Node(value)

        def walk(root, new):
            if not root:
                return
            if new_n.value < root.value:
                if not root.left:
                    root.left = new_n
                else:
                    walk(root.left, new_n)
            else:
                if not root.right:
                    root.right = new_n
                else:
                    walk(root.right, new_n)
        if not self.root:
            self.root = new_n
            return self.root
        walk(self.root, new_n)
