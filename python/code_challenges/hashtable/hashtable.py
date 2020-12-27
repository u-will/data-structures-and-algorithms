from linked_list import LinkedList

class Hashtable:

    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]
        # you can also see a bucket as a hashmap = [[] for _ in range (0, self.size)]

    def _hash(self, key):
        sum = 0
        for ch in key:
            sum += ord(ch)

        primed = sum * 19
        index = primed % self._size

        return index

    def contains (self, requesting_key):
        hashed_key_index = self._hash(requesting_key)
        bucket = self._buckets[hashed_key_index]
        current = bucket.head
        while current:
            # in the linked list that we are using here, they call the value of the node data (so instead of current.value, we will say current.data)
            pair = current.data # [key, value]
            stored_key = pair[0]
            stored_value = pair[1]

            if stored_key == requesting_key:
                return True
            current = current.next
        return False

    def get (self, requesting_key):
        hashed_key_index = self._hash(requesting_key)
        bucket = self._buckets[hashed_key_index] #Linked list

        current = bucket.head
        while current:
            # in the linked list that we are using here, they call the value of the node data (so instead of current.value, we will say current.data)
            pair = current.data # [key, value]
            stored_key = pair[0]
            stored_value = pair[1]

            if stored_key == requesting_key:
                return stored_value
            current = current.next



    def add(self, key, value):
        hashed_key_index = self._hash(key)

        if not self._buckets[hashed_key_index]:
           self._buckets[hashed_key_index] = LinkedList()

        self._buckets[hashed_key_index].add((key, value))



