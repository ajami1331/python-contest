import sys
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
        if a != b:
            if self.sz[a] < self.sz[b]:
                a, b = b, a
            self.par[b] = a
            self.sz[a] += self.sz[b]
            self.num_sets -= 1
class solution:
    def __init__(self) -> None:
        pass
    def solve(self, input, output) -> None:
        n = int(input())
        dsu_ = dsu(n)
        ar = list(map(int, input().split()))
        for i in range(n):
            dsu_.union(i, ar[i] - 1)
        print(dsu_.num_sets, file=output)

if __name__ == "__main__":
    s = solution()
    s.solve(sys.stdin.buffer.readline, sys.stdout)