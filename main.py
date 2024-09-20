#!/usr/bin/env python3

from solution import solution

def validate_case(tc):
    # compare the output with the expected output
    with open(f"test_cases/{tc}.out", "r") as output_file, open(f"test_cases/{tc}.val", "r") as expected_file:
        output = output_file.read()
        expected = expected_file.read()
        if output == expected:
            print(output)
            # green color
            print("\033[92m", end="")
            print(f"Test case {tc} passed")
            # reset the color
            print("\033[0m", end="")
        else:
            # red color
            print("\033[91m", end="")
            print(f"Test case {tc} failed")
            # reset the color
            print("\033[0m", end="")
            print(f"Output: {output}")
            print(f"Expected: {expected}")
        print("--------------------")

def run_case(tc):
     # read a test case from test_cases/tc{tc}
    with open(f"test_cases/{tc}.in", "r") as input_file, open(f"test_cases/{tc}.out", "w") as output_file:
        s.solve(input_file.readline, output_file)
    validate_case(tc)

if __name__ == "__main__":
    s = solution()
    # read a int from test_cases/cnt 
    print("--------------------")
    with open("test_cases/cnt", "r") as f:
        cnt = int(f.readline())
    for tc in range(1, cnt + 1):
       run_case(tc)