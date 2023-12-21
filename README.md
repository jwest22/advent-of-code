# 2023 Advent of Code

## Day 3 Part 1

1. **pivot_file_contents_by_character(file_path)**: Reads a text file, removes line breaks, and replaces all non-numeric characters with 'g'. Returns a DataFrame with each character and its corresponding ID.
2. **get_ids_of_non_integer_characters(df)**: Returns a list of IDs where the character is 'g'.
3. **apply_calculations_to_ids(ids)**: Applies a set of calculations to the given list of IDs and returns the calculated values.
4. **get_combined_integer_ids(df)**: Extracts combined integer values from the DataFrame and groups their corresponding IDs.
5. **lookup_combined_integers(calculated_ids, combined_integer_ids)**: Looks up the combined integer values based on calculated IDs and returns these integers.

## Day 3 Part 2
**Note:** Oh well, grid traversal it is. 

- Reads a grid of characters from a specified file.
- Searches for occurrences of a specified target character (e.g., `*`).
- For each occurrence of the target character, the function identifies all numbers (one or more digits) adjacent to it in all eight directions.
- If a target character is adjacent to two or more numbers, the function calculates the product of these numbers.
- Summarizes the products of all such sets of numbers and prints the total sum.

## Day 4 Part 1

- **sum_points(file_path)**: Reads data from a file, where each line contains two parts separated by a '|'. For each line, it splits the parts, creates sets from the numbers in each part, and calculates the number of points based on the intersection of these sets. The points for each line are calculated as follows: 1 point for a single match, and 2^(matches-1) points for more than one match. Returns the total points calculated from all lines in the file.

## Day 8 Part 1

- **navigate_network_from_file(file_path)**: Reads a network structure and instructions from a file at `file_path`. The first line of the file is expected to contain instructions, and subsequent lines should define network connections. Initiates the navigation process starting from a predetermined node ('AAA') and following the instructions. Returns the total number of steps taken to reach a specified endpoint ('ZZZ') in the network.

    - **navigate_network(start_node, instructions)**: This function is defined within `navigate_network_from_file`. It navigates through the network starting from `start_node`, following the given `instructions`. The function iterates over each instruction to move through the network and increments a step counter. Navigation ends when the endpoint ('ZZZ') is reached. Returns the total number of steps taken.

## Day 8 Part 2

1. **lcm(a, b)**: Calculates the Least Common Multiple (LCM).
2. **lcm_of_list(numbers)**: Calculates the LCM of a list of integers. Takes list `numbers` as input and returns the LCM.
3. **parse_graph_from_file(file_path)**: Parses a graph from a text file. The file should contain instructions on the first line and graph edges on subsequent lines. Returns a tuple containing the graph (as a dictionary) and the instructions.
4. **find_start_nodes(graph)**: Identifies and returns a list of all nodes in the given `graph` that end with the letter 'A' as starting points.
5. **find_paths_with_instructions(graph, start_node, instructions)**: Finds a path in the `graph` starting from `start_node` and following the given `instructions`. The path-finding process continues until a node ending with 'Z' is reached. Returns the list of nodes in the found path.
6. **calculate_lcm_of_paths(graph, start_nodes, instructions)**: Calculates the LCM of the lengths of paths starting from each node in `start_nodes` and following the `instructions`. Returns the LCM of these path lengths as an integer.
