from random import randint

class TreapNode(object):
    def __init__(self, key):
        self.key = str(key)
        self.priority = randint(1, 100)
        self.size = 1
        self.left = None
        self.right = None
    #
    def set_left(self, left):
        self.left = left
        self.update_size()
    #
    def set_right(self, right):
        self.right = right
        self.update_size()
    #
    def update_size(self):
        self.size = 1
        if self.left: self.size += self.left.size
        if self.right: self.size += self.right.size
    #
    def split(self, key):
        if int(self.key) < int(key):
            r_split = self.right.split(key) if self.right else (None, None)
            self.set_right(r_split[0])
            return (self, r_split[1])
        else:
            l_split = self.left.split(key)
            self.set_left(l_split[1]) if self.left else (None, None)
            return (l_split[0], self)
    #
    def insert(self, _new):
        if self.priority < _new.priority:
            splitted = self.split(_new.key)
            _new.set_left(splitted[0])
            _new.set_right(splitted[1])
            return _new
        elif int(_new.key) < int(self.key):
            self.set_left(self.left.insert(_new) if self.left else _new)
        else:
            self.set_right(self.right.insert(_new) if self.right else _new)
        return self
    #
    def merge(self, other):
        if other is None: return self
        if self.priority < other.priority:
            other.set_left(self.merge(other.left))
            return other
        else:
            self.set_right(self.right.merge(other) if self.right else other)
            return self
    #
    def erase(self, key):
        if self.key == key:
            result = self.left.merge(self.right) if self.left else self.right
            return result
        elif int(key) < int(self.key):
            self.set_left(self.left.erase(key) if self.left else None)
        else:
            self.set_right(self.right.erase(key) if self.right else None)
        return self
    #
    def get_kth(self, k):
        if k > self.size:
            return None
        left_size = 0
        if self.left is not None: left_size = self.left.size
        if k <= left_size:
            return self.left.get_kth(k) if self.left else self
        elif k == left_size + 1:
            return self
        else:
            return self.right.get_kth(k - left_size - 1) if self.right else None
    #
    def count_less_than(self, key):
        if int(self.key) >= int(key):
            return self.left.count_less_than(key) if self.left else 0
        else:
            left_size = self.left.size if self.left else 0
            return left_size + 1 + (self.right.count_less_than(key) if self.right else 0)
    #
    def __str__(self):
        str_list = []
        str_list.append(self.key)
        if self.left: str_list.append(str(self.left))
        if self.right: str_list.append(str(self.right))
        return '[' + (', '.join(str_list)) + ']'
    #
    def __repr__(self):
        return str(self)
