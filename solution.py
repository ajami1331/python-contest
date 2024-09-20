import sys
import sys
import library.dsu as dsu

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