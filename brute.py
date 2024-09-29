#!/usr/bin/env python3
import collections
import sys
import heapq
import math

def solve_case():
    b, c, d = map(int, input().split())
    for a in range(0, 1000):
        tmp = d - (a | b) + (a & c)
        if tmp == 0:
            print(a)
            return
    print(-1)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve_case()