def sum_points(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_points = 0

    for line in lines:
        part1, part2 = line.split('|')

        set1 = set(map(int, part1.split()[2:]))
        set2 = set(map(int, part2.split()))

        matches = set1.intersection(set2)

        amt_matches = len(matches)
        if amt_matches == 1:
            points = 1
        elif amt_matches > 1:
            points = 2**(amt_matches-1)
        else:
            points = 0
        total_points += points

    return total_points

print(sum_points('4_input.txt'))
