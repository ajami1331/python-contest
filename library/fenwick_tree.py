class fenwick_tree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def sum(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

    def add(self, idx, delta):
        while idx <= self.n:
            self.bit[idx] += delta
            idx += idx & -idx

    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

    def point_query(self, idx):
        return self.range_sum(idx, idx)

    def point_update(self, idx, delta):
        self.add(idx, delta - self.point_query(idx))

    def lower_bound(self, x):
        sum = 0
        pos = 0
        for i in range(20, -1, -1):
            if pos + (1 << i) < self.n and sum + self.bit[pos + (1 << i)] < x:
                sum += self.bit[pos + (1 << i)]
                pos += (1 << i)
        return pos + 1

    def upper_bound(self, x):
        return self.lower_bound(x + 1)ß
