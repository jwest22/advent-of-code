# 2023 Advent of Code

## Day 3 Part 1
1. **pivot_file_contents_by_character(file_path)**: Reads a text file, removes line breaks, and replaces all non-numeric characters with 'g'. Returns a DataFrame with each character and its corresponding ID.
2. **get_ids_of_non_integer_characters(df)**: Returns a list of IDs where the character is 'g'.
3. **apply_calculations_to_ids(ids)**: Applies a set of calculations to the given list of IDs and returns the calculated values.
4. **get_combined_integer_ids(df)**: Extracts combined integer values from the DataFrame and groups their corresponding IDs.
5. **lookup_combined_integers(calculated_ids, combined_integer_ids)**: Looks up the combined integer values based on calculated IDs and returns these integers.
