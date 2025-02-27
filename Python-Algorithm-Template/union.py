class UnionFind:
    def __init__(self):
        self.parent = {}
        self.count = 0

    def add(self, pos):
        if pos not in self.parent:
            self.parent[pos] = pos
            self.count += 1

    def find(self, pos):
        if self.parent[pos] != pos:
            self.parent[pos] = self.find(self.parent[pos]) # path compression
        return self.parent[pos]

    def union(self, pos1, pos2):
        root1, root2 = self.find(pos1), self.find(pos2)
        if root1 != root2:
            self.parent[root2] = root1
            self.count -= 1

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.count