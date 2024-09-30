#!/usr/bin/env python3
import sys
import math
import random
from library.segtree import segtree

class solution:
    lim = 2 * 10 ** 5 + 5
    def __init__(self) -> None:
        pass
    def solve(self, input, output) -> None:
        self.solve_case(input, output)
    def solve_case(self, input, output) -> None:
        n, q = map(int, input().split())
        ar = list(map(int, input().split()))
        st = segtree.from_array(ar, lambda a, b: a + b, 0)
        for _ in range(q):
            t, x, y = map(int, input().split())
            if t == 1:
                output.write(f"{st.prod(x, y)}\n")
            else:
                ar[x] += y
                st.set(x, ar[x])

if __name__ == "__main__":
    s = solution()
    s.solve(sys.stdin.buffer.readline, sys.stdout)
