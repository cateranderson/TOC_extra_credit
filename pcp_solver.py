import sys
from collections import deque

def solve_pcp(tiles, max_steps=10000):
    """
    Solves the Post Correspondence Problem using BFS.
    Args:
        tiles (list of tuples): Each tuple contains (top, bottom) strings.
        max_steps (int): Limit on the number of steps to avoid infinite loops.
    Returns:
        list: A list of solutions where each solution is a list of tile indices.
    """
    queue = deque([("", "", [])])  # (current_top, current_bottom, sequence_of_indices)
    solutions = []
    visited = set()

    steps = 0
    while queue and steps < max_steps:
        steps += 1
        current_top, current_bottom, sequence = queue.popleft()

        # If the top and bottom match (non-empty), we have a solution
        if current_top == current_bottom and current_top != "":
            solutions.append(sequence)
            continue

        # Iterate through all tiles
        for i, (top, bottom) in enumerate(tiles):
            new_top = current_top + top
            new_bottom = current_bottom + bottom
            # Only continue if the strings are "prefix-compatible"
            if new_top.startswith(new_bottom) or new_bottom.startswith(new_top):
                state = (new_top, new_bottom)
                if state not in visited:
                    visited.add(state)
                    queue.append((new_top, new_bottom, sequence + [i + 1]))  # Use 1-based index

    return solutions

def read_input_file(filename):
    """
    Reads input file containing multiple test cases.
    Args:
        filename (str): Path to the input file.
    Returns:
        list: A list of test cases, where each test case is a list of (top, bottom) pairs.
    """
    test_cases = []
    with open(filename, 'r') as f:
        current_case = []
        for line in f:
            line = line.strip()
            if line == "" or line == "---":  # Empty line or delimiter signals new test case
                if current_case:  # Save the previous test case
                    test_cases.append(current_case)
                    current_case = []
            else:
                top, bottom = line.split("/")
                current_case.append((top, bottom))
        if current_case:  # Add the last test case
            test_cases.append(current_case)
    return test_cases

def main(input_file):
    """
    Main function to read input file, solve PCP for each test case, and print results.
    Args:
        input_file (str): Path to the input file.
    """
    test_cases = read_input_file(input_file)
    for idx, tiles in enumerate(test_cases, 1):
        print(f"Test Case {idx}:")
        solutions = solve_pcp(tiles)
        if solutions:
            for sol in solutions:
                print(f"  Solution: {sol}")
        else:
            print("  No solution found.")
        print()

if __name__ == "__main__":
    input_file = sys.argv[1]  # Pass input file as a command line argument
    main(input_file)

