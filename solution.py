#!/usr/bin/env python3
import sys

class solution:
    cnt = 0

    def __init__(self) -> None:
        pass

    def solve(self, input, output) -> None:
        t = int(input())
        for _ in range(t):
            self.solve_case(input, output)

    def ask(self, input, output, s) -> int:
        output.write(f"? {s}\n")
        output.flush()
        self.cnt += 1
        return int(input())

    def solve_case(self, input, output) -> None:
        n = int(input())
        if n == -1:
            raise Exception("invalid input")
        ans = ""
        self.cnt = 0
        # going forward
        while len(ans) < n:
            # try 0
            if self.ask(input, output, ans + "0") == 1:
                ans = ans + "0"
                continue
            # try 1
            if self.ask(input, output, ans + "1") == 1:
                ans = ans + "1"
                continue
            break
        # going backward
        while len(ans) < n:
            # try 0
            if self.ask(input, output, "0" + ans) == 1:
                ans = "0" + ans
                continue
            else:
                ans = "1" + ans
                continue
        output.write(f"! {ans}\n")
        output.flush()


if __name__ == "__main__":
    s = solution()
    s.solve(sys.stdin.buffer.readline, sys.stdout)
