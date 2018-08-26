# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key
# if the key exists in the cache, otherwise return -1.
#
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate
# the least recently used item before inserting a new item.
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


# Solution reference:
# https://medium.com/@krishankantsinghal/my-first-blog-on-medium-583159139237


class Entry(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache_ref = {}
        self.curr_size = 0

    def addToHead(self, entry):
        entry.right = self.head
        entry.left = None
        if self.head is not None:
            self.head.left = entry
        self.head = entry
        if self.tail is None:
            self.tail = entry

    def remove(self, entry):
        if entry.left is not None:
            entry.left.right = entry.right
        else:
            self.head = entry.right
        if entry.right is not None:
            entry.right.left = entry.left
        else:
            self.tail = entry.left

    def get(self, key):
        if key in self.cache_ref:
            entry = self.cache_ref[key]
            self.put(entry.key, entry.val)
            return entry.val
        return -1

    def put(self, key, value):
        if key in self.cache_ref:
            entry = self.cache_ref[key]
            entry.val = value
            self.remove(entry)
            self.addToHead(entry)
        else:
            entry = Entry(key, value)
            self.cache_ref[key] = entry
            if self.curr_size < self.capacity:
                self.addToHead(entry)
                self.curr_size += 1
            else:
                del self.cache_ref[self.tail.key]
                self.remove(self.tail)
                self.addToHead(entry)


def test():
    # cache = LRUCache(2)
    #
    # cache.put(1, 1)
    # cache.put(2, 2)
    # cache.get(1)       // returns 1
    # cache.put(3, 3)    // evicts key 2
    # cache.get(2)       // returns -1 (not found)
    # cache.put(4, 4)    // evicts key 1
    # cache.get(1)       // returns -1 (not found)
    # cache.get(3)       // returns 3
    # cache.get(4)       // returns 4
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    print 'test success!'


if __name__ == '__main__':
    test()  # run
