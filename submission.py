#!/usr/bin/env python3
import sys
import math
import random
class segtree:
    def __init__(self, n, op, e):
        self._n = n
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._op = op
        self._e = e
        self._d = [e] * (2 * self._size)

    @classmethod
    def from_array(cls, arr, op, e):
        n = len(arr)
        seg = cls(n, op, e)
        seg._d[seg._size:seg._size + n] = arr
        for i in range(seg._size - 1, 0, -1):
            seg._update(i)
        return seg
        
    def set(self, p, x):
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)
    
    def get(self, p):
        return self.d[p + self._size]
    
    def prod(self, l, r):
        sml = smr = self._e
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                smr = self._op(self._d[r - 1], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    def all_prod(self):
        return self._d[1]

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

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
