#!/usr/bin/env python3
import sys
import math
import random
import library.fastio as fastio

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
