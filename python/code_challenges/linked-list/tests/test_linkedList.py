from linked_list.linked_list import Node, LinkedList

def test_instantiation():
	initialList = LinkedList()
	assert initialList.head == None

def test_multiple_ins():
	initialList = LinkedList()
	initialList.insert(9)
	initialList.insert(2)
	assert initialList.head.value == 2 and initialList.head.next
    
    
def test_insertion():
	initialList = LinkedList()
	initialList.insert(7)
	assert initialList.head.value == 7



def test_return_all_values():
	initialList = LinkedList()
	initialList.insert(5)
	initialList.insert(6)
	initialList.insert(7)
	initialList.insert(8)
	assert str(initialList) == '8 ->7 ->6 ->5 ->NULL'
