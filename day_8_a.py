def navigate_network_from_file(file_path):
    with open(file_path, 'r') as file:
        network_input = file.read()

    lines = network_input.strip().split("\n")

    # First line contains the instructions
    instructions = lines[0].strip()

    connections = {}
    for line in lines[1:]:
        if "=" not in line or not line.strip():
            continue

        node, edges = line.split("=")
        connections[node.strip()] = tuple(edges.strip(" ()").split(", "))

    def navigate_network(start_node, instructions):
        current_node = start_node
        total_steps = 0 

        while True:
            for instr in instructions:
                next_node = connections[current_node][0 if instr == 'L' else 1]
                current_node = next_node
                total_steps += 1

                if current_node == 'ZZZ':
                    return total_steps 

    start_node = 'AAA'
    return navigate_network(start_node, instructions)

steps = navigate_network_from_file("8_input.txt")
print(steps)
