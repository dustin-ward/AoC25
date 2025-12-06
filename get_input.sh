#!/usr/bin/bash
if [ -z "$1" ]; then
    echo "No day supplied"
    exit 1
fi

day=$1
mkdir ./$day
cookie="53616c7465645f5f444db361e4e200df0e73ab38c5c21742ba1b4c64d7daccfabcce9821a66eaddb0c975313cebf3686ec9993d32d287d480f5b692e25aebc04"

echo "Downloading input for day $day..."
curl -H "Cookie: session=$cookie" "https://adventofcode.com/2025/day/$day/input" > ./$day/full_input.txt
echo "Done"

