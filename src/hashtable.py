# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # append an item at the end of our linked pair chain. if the item exists overwrite it
    def append(self, key, value):
        if self.key == key:
            self.value = value
        elif not self.next:
            self.next = LinkedPair(key, value)
        else:
            self.next.append(key, value)

    # retrieve an item from our linked list chain
    def retrieve(self, key):
        if self.key == key:
            return self.value
        elif not self.next:
            print(f"Hash[{key}] is undefined")
            return None
        else:
            return self.next.retrieve(key)


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        if not None in self.storage:
            self.resize()
        index = self._hash_mod(key)

        # if we have something at the index, append this value. Using linkedpair.append will
        # overwrite a value already existing, and traverse over all the values
        if self.storage[index]:
            self.storage[index].append(key, value)
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # if there is nothing at our index, print our little error message and get out of there!
        if not self.storage[index]:
            print(f"WARNING: Item with key {key} not found")
            return
        current_node = self.storage[index]
        prev_node = None
        # if there is only one node at this index and it has the key we want we just need to delete it, make the value at this index None
        if current_node.key == key and not current_node.next:
            self.storage[index] = None
        elif current_node.key == key:
            self.storage[index] = self.storage[index].next
        else:
            while current_node:
                if current_node.key == key:
                    prev_node.next = current_node.next
                    return
                prev_node = current_node
                current_node = current_node.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index]:
            return self.storage[index].retrieve(key)
        else:
            print(f"Hash[{key}] is not found")

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        old_storage = self.storage
        self.storage = [None] * self.capacity
        for node in old_storage:
            if node:
                current_node = node
                while current_node:
                    self.insert(current_node.key, current_node.value)
                    current_node = current_node.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
