import sys
import math

class solution:
    def __init__(self) -> None:
        pass

    def solve(self, input, output) -> None:
        t = int(input())
        for _ in range(t):
            self.solve_case(input, output)

    def solve_case(self, input, output) -> None:
        n = int(input())
        ar = list(map(int, input().split()))
        ans = 0
        max_iter = int(math.log2(n) + 10)
        for iteration in range(max_iter):
            for i in range(n - 1):
                if ar[i] > ar[i + 1]:
                    dif = ar[i] - ar[i + 1]
                    ar[i] -= dif // 2
                    ar[i + 1] += dif // 2
                    if dif % 2 != 0:
                        ar[i] -= 1
                        ar[i + 1] += 1
        ans = max(ar) - min(ar)
        output.write(f"{ans}\n")


if __name__ == "__main__":
    s = solution()
    s.solve(sys.stdin.buffer.readline, sys.stdout)
