from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_of_list(numbers):
    return reduce(lcm, numbers, 1)

def parse_graph_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    instructions = lines[0].strip()
    graph = {}
    for line in lines[1:]:
        line = line.strip()
        if '=' in line:
            node, edges = line.split(' = ')
            edges = tuple(edges.strip('()').split(', '))
            graph[node.strip()] = edges

    return graph, instructions

def find_start_nodes(graph):
    return [node for node in graph if node.endswith('A')]

def find_paths_with_instructions(graph, start_node, instructions):
    path = [start_node]
    step = 0
    instruction_length = len(instructions)

    # Continue until a node ending with 'Z' is reached
    while not path[-1].endswith('Z'):
        direction = 0 if instructions[step % instruction_length] == 'L' else 1  # Cycle through instructions
        next_node = graph[path[-1]][direction]
        path.append(next_node)
        step += 1

    return path

def calculate_lcm_of_paths(graph, start_nodes, instructions):
    cycle_lengths = [len(find_paths_with_instructions(graph, node, instructions)) - 1 for node in start_nodes]
    return lcm_of_list(cycle_lengths)

file_path = '8_input.txt'
graph, instructions = parse_graph_from_file(file_path)
start_nodes = find_start_nodes(graph)
print(start_nodes)
total_steps = calculate_lcm_of_paths(graph, start_nodes, instructions)

print("Total steps to simultaneously reach 'Z':", total_steps)
#13663968099527
