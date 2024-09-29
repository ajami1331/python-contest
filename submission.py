#!/usr/bin/env python3
import sys
import math
import random
class dsu:
    def __init__(self, n):
        self.reset(n)

    def reset(self, n):
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

class solution:
    lim = 2 * 10**5
    def __init__(self) -> None:
        pass
    def solve(self, input, output) -> None:
        t = int(input())
        for _ in range(t):
            self.solve_case(input, output)
    def solve_case(self, input, output) -> None:
        n, m = map(int, input().split())
        ar = [[0 for x in range(12)] for _ in range(n + 2)]
        ds = dsu(n + 1)
        for q in range(m):
            a, d, k = map(int, input().split())
            ar[a][d] = max(ar[a][d], a + k * d)
        for i in range(1, n + 1):
            for j in range(1, 11):
                if i - j > 0:
                    ar[i][j] = max(ar[i][j], ar[i - j][j])
                if i + j <= n and i + j <= ar[i][j]:
                    ds.union(i, i + j)
        output.write(str(ds.num_sets - 1) + "\n")


if __name__ == "__main__":
    s = solution()
    s.solve(sys.stdin.buffer.readline, sys.stdout)
