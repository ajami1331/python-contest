#!/usr/bin/env python3

import sys
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
        sys.stdin = input_file
        sys.stdout = output_file
        solution().solve()
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    validate_case(tc)


def recurse_imports(file: str, cache: set) -> str:
    code = ""
    if file in cache:
        return code
    cache.add(file)
    with open(file, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            if line.startswith("import library."):
                line = line.removeprefix("import ")
                file_to_import = line.split(" as ")[0]
                file_to_import = file_to_import.replace(".", "/")
                code += recurse_imports(f"{file_to_import}.py", cache)
                continue
            elif line.startswith("from library."):
                line = line.removeprefix("from ")
                file_to_import = line.split(" import ")[0]
                file_to_import = file_to_import.replace(".", "/")
                code += recurse_imports(f"{file_to_import}.py", cache)
                continue
            elif line not in cache and (line.startswith("import ") or line.startswith("from ")):
                code += line
                cache.add(line)
                continue
            elif line not in cache:
                code += line
    return code


def create_file_for_submission():
    with open("submission.py", "w") as f:
        f.write(recurse_imports("solution.py", set()))


if __name__ == "__main__":
    # read a int from test_cases/cnt
    print("--------------------")
    with open("test_cases/cnt", "r") as f:
        cnt = int(f.readline())
    for tc in range(1, cnt + 1):
        run_case(tc)
    create_file_for_submission()
