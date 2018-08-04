class DisjointSet(object):
    def __init__(self, n):
        self.parents = range(n)
        self.ranks = [1] * n
        self.sizes = [1] * n

    def find(self, u):
        """Find root of u, and flatten out tree by
        setting all descendants of root to point root as direct parent
        """
        if u == self.parents[u]:
            return u
        result = self.parents[u] = self.find(self.parents[u])
        return result

    def merge(self, u, v):
        """Merge two different trees"""
        u_root = self.find(u)
        v_root = self.find(v)
        if u_root == v_root:
            return
        if self.ranks[u_root] > self.ranks[v_root]:
            u_root, v_root = v_root, u_root
        self.parents[u_root] = v_root
        self.sizes[v_root] += self.sizes[u_root]
        if self.ranks[u_root] == self.ranks[v_root]:
            self.ranks[v_root] += 1

    def get_size(self, u):
        """Get size of set which contains u"""
        return self.sizes[self.find(u)]
