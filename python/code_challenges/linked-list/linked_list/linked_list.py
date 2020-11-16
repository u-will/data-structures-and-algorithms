class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,value):
     node = Node(value)
     node.next = self.head
     self.head = node

    def includes(self, val):
        current = self.head
        while current != None:
            if current.value == val :
                return True
            else:
                current = current.next
        return False
    def __str__(self):
        result =""
        current = self.head
        while current != None:
            result +=f"{current.value} ->"
            current = current.next
        result += "NULL"
        return result
