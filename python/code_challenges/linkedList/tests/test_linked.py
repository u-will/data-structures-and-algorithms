from linkedlist.linkedlist import Node, LinkedList

def test_instantiation():
	initialList = LinkedList()
	assert initialList.head == None

def test_append():
	initialList = LinkedList()
	initialList.append(5)
	initialList.append(6)
	initialList.append(7)
	initialList.append(8)
	assert str(initialList) == '5 ->6 ->7 ->8'

def test_insert_before():
	initialList = LinkedList()
	initialList.append(5)
	initialList.append(6)
	initialList.append(8)
    initialList.insert_before(7, 6)
	assert str(initialList) == '5 ->6 ->8'

def test_insert_after():
	initialList = LinkedList()
	initialList.append(5)
	initialList.append(6)
	initialList.append(8)
	initialList.insert_after(7, 6)
	assert str(initialList) == '5 ->6 ->7 ->8'


