#!/usr/bin/env python3
import sys
import math
import random
import os
from io import BytesIO, IOBase

FAST_IO_BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, FAST_IO_BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, FAST_IO_BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def m(x: int) -> int:
    return 1 << x


class solution:
    lim = 2 * 10**5 + 5
    end_states = []

    def __init__(self) -> None:
        pass

    def solve(self) -> None:
        self.end_states.append(m(0) | m(1) | m(2))
        self.end_states.append(m(3) | m(4) | m(5))
        self.end_states.append(m(6) | m(7) | m(8))

        self.end_states.append(m(0) | m(3) | m(6))
        self.end_states.append(m(1) | m(4) | m(7))
        self.end_states.append(m(2) | m(5) | m(8))

        self.end_states.append(m(0) | m(4) | m(8))
        self.end_states.append(m(6) | m(4) | m(2))
        n = int(input())
        for _ in range(n):
            self.solve_case(_)

    def solve_case(self, cs) -> None:
        board = 0
        for x in range(3):
            line = str(input().strip())
            for x in range(3):
                board = board << 1
                if line[x] == "X":
                    board |= 1
        print("Game #{}: ".format(cs + 1), end="")
        print("Alice" if self.winner(board) else "Bob")

    def winner(self, board):
        ret = False
        if self.game_over(board):
            return True
        for i in range(9):
            if (board & m(i)) == 0:
                ret |= not self.winner(board | m(i))
        return ret

    def game_over(self, board):
        for x in self.end_states:
            if (board & x) == x:
                return True
        return False

if __name__ == "__main__":
    solution().solve()
