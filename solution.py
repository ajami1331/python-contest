import sys

class solution:
    def __init__(self) -> None:
        pass
    def solve(self, input, output) -> None:
        n = int(input())
        if n % 2 == 0 and n > 2:
            output.write("YES\n")
        else:
            output.write("NO\n")

if __name__ == "__main__":
    s = solution()
    s.solve(sys.stdin.buffer.readline, sys.stdout)