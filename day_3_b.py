def find_adjacent_numbers_from_file(file_name, target_char):
    with open(file_name, 'r') as file:
        string_array = file.readlines()
        string_array = [line.strip() for line in string_array]

    grid = [list(row) for row in string_array]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    def extract_full_number(i, j):
        if not grid[i][j].isdigit():
            return None
        num = grid[i][j]
        x = j - 1
        while x >= 0 and grid[i][x].isdigit():
            num = grid[i][x] + num
            x -= 1
        x = j + 1
        while x < cols and grid[i][x].isdigit():
            num += grid[i][x]
            x += 1
        return num

    star_adjacent_numbers = {}
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == target_char:
                adjacent_numbers = set()
                directions = [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
                for x, y in directions:
                    if 0 <= x < rows and 0 <= y < cols:
                        number = extract_full_number(x, y)
                        if number is not None:
                            adjacent_numbers.add(number)
                if adjacent_numbers:
                    star_adjacent_numbers[(i, j)] = adjacent_numbers

    total_sum = 0
    for coords, numbers in star_adjacent_numbers.items():
        if len(numbers) >= 2:
            product = 1
            for number in numbers:
                product *= int(number)
            total_sum += product
            print(f"({coords[0]}, {coords[1]}): {', '.join(numbers)}, Product: {product}")

    print(f"Total Sum of Products: {total_sum}")

find_adjacent_numbers_from_file("3_input.txt", "*")
