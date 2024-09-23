#!/bin/bash

rm -rf random_tests
mkdir random_tests

for((i = 1; ; ++i)); do
    python3 ./gen.py $i > random_tests/input
    python3 ./submission.py < random_tests/input > random_tests/output
    python3 ./brute.py < random_tests/input > random_tests/correct
    if (! diff random_tests/output random_tests/correct); then
        echo "WA"
        cat random_tests/input
        break
    fi
    echo "Test $i passed"
done