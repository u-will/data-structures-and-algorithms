class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head == None :
            return
        current = self.head
        retStr = str(current)
        while current.next:
            current.next
            retStr += " ->"+ str(current)
        return retStr

    def append(self, value):
        current = self.head
        while current != None:
            if current.next == None:
                current.next = Node(value)
                break
            else:
                current = current.next

    def insert_before(self, value, newVal):
        if self.head.value == value :
            temp = self.head
            temp.value = self.head.value
            self.head = Node(newVal, temp)
        else:
            current = self.head
            while current.next.value != value:
                if current.next.next.value == value:
                    tempVal= current.next.value
                    newNode = Node(newVal, current.next.next)
                    current.next = Node(tempVal, newNode)
                    break
                else:
                    current = current.next

    def insert_after(self, value, newVal):
        current = self.head
        if current.value == value :
            tempVal= current.next.value
            newNode = Node(newVal, current.next.next)
            current.next = Node(tempVal, newNode)
        else:
            while current != value :
                if current.next == value:
                    tempVal = current.next.next.val
                    newNode = Node (newVal, current.next.next.next)
                    current.next.next = Node(tempVal, newNode)
                    break
                else:
                    current = current.next


