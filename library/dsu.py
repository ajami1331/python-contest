class dsu:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.sz = [1 for i in range(n)]
        self.num_sets = n

    def find(self, a):
        if self.par[a] == a:
            return a
        self.par[a] = self.find(self.par[a])
        return self.par[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.par[b] = a
        self.sz[a] += self.sz[b]
        self.num_sets -= 1
