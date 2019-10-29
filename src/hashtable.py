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
        self.count = 0
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
        if self.count >= self.capacity:
            self.resize()

        index = self._hash_mod(key)
        new_item = LinkedPair(key, value)

        if self.storage[index] is not None:
            current_head = self.storage[index]
            current = self.storage[index].next
            while current:
                current = current.next
            current = current_head
            self.storage[index] = new_item
            self.count += 1
        else:
            self.storage[index] = new_item
            self.count += 1

        # n = 0
        # for i in self.storage:
        #     if i is None:
        #         self.storage[self.count] = new_item
        #         self.count += 1
        #         return
        #     elif i.key == key:
        #         self.storage[n] = new_item
        #         return
        #     n += 1

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        i = 0
        for item in self.storage:
            if item is not None:
                if key == item.key:
                    self.storage[i] = None
            i += 1
        print("WARNING: Item with that key not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        for n in self.storage:
            if n is not None:
                if key == n.key:
                    return n.value
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.storage.extend([None] * self.capacity)
        self.capacity *= 2


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
