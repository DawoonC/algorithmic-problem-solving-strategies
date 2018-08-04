class RangeMinQuery(object):
    """Range Minimum Query (RMQ) is a binary tree for
    quickly searching minimum value of a given range (left, right).

    Since RMQ is a balanced binary tree, we can represent it
    with a normal list, just like a heapq.
    """
    def __init__(self, array):
        self.n = len(array)
        self.range_min = [None] * (self.n * 4)
        self.create(array, 0, self.n - 1, 1)

    def create(self, array, left, right, node):
        if left == right:
            result = self.range_min[node] = array[left]
            return result
        mid = (left + right) / 2
        left_min = self.create(array, left, mid, node * 2)
        right_min = self.create(array, mid + 1, right, (node * 2) + 1)
        result = self.range_min[node] = min(left_min, right_min)
        return result

    def query_min(self, left, right, node, node_left, node_right):
        # in case of invalid range
        if right < node_left or node_right < left:
            return float('inf')
        if left <= node_left and node_right <= right:
            return self.range_min[node]
        mid = (node_left + node_right) / 2
        return min(self.query_min(left, right, node * 2, node_left, mid),
                   self.query_min(left, right, (node * 2) + 1, mid + 1, node_right))

    def query(self, left, right):
        return self.query_min(left, right, 1, 0, self.n - 1)

    def update_min(self, index, new_value, node, node_left, node_right):
        if index < node_left or node_right < index:
            return self.range_min[node]
        if node_left == node_right:
            result = self.range_min[node] = new_value
            return result
        mid = (node_left + node_right) / 2
        result = self.range_min[node] = min(
            self.update_min(index, new_value, node * 2, node_left, mid),
            self.update_min(index, new_value, (node * 2) + 1, mid + 1, node_right)
        )
        return result

    def update(self, index, new_value):
        self.update_min(index, new_value, 1, 0, self.n - 1)

    def __repr__(self):
        return str([e for e in self.range_min if e is not None])
