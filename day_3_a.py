import pandas as pd
import re

def pivot_file_contents_by_character(file_path):
    with open(file_path, 'r') as file:
        text = file.read().replace('\n', '').replace('\r', '')
        text = re.sub(r'[^0-9.]', 'g', text)
    return pd.DataFrame({'ID': range(1, len(text) + 1), 'Character': list(text)})

def get_ids_of_non_integer_characters(df):
    return df[df['Character'].str.match(r'^g$', case=False)]['ID'].tolist()

def apply_calculations_to_ids(ids):
    calculations = [-141, -140, -139, -1, 1, 139, 140, 141]
    calculated_values = set()

    for id_value in ids:
        calculated_values.update(id_value + calc for calc in calculations)

    return sorted(calculated_values)

def get_combined_integer_ids(df):
    combined_integers = {}
    current_number = ''
    current_ids = []

    for row in df.itertuples():
        if row.Character.isdigit():
            current_number += row.Character
            current_ids.append(row.ID)
        elif current_number:
            if int(current_number) in combined_integers:
                combined_integers[int(current_number)].append(current_ids)
            else:
                combined_integers[int(current_number)] = [current_ids]
            current_number = ''
            current_ids = []

    if current_number:
        if int(current_number) in combined_integers:
            combined_integers[int(current_number)].append(current_ids)
        else:
            combined_integers[int(current_number)] = [current_ids]

    return combined_integers

def lookup_combined_integers(calculated_ids, combined_integer_ids):
    found_integers = []
    id_sets_used = set()

    for calc_id in calculated_ids:
        for integer, id_sets in combined_integer_ids.items():
            for id_set in id_sets:
                id_set_tuple = tuple(id_set)  # Convert list to tuple for set operations
                if calc_id in id_set and id_set_tuple not in id_sets_used:
                    found_integers.append(integer)
                    id_sets_used.add(id_set_tuple)

    return found_integers

file_path = '3_input.txt'

df_pivoted_chars = pivot_file_contents_by_character(file_path)
df_pivoted_chars.to_csv('out.csv')
non_integer_ids = get_ids_of_non_integer_characters(df_pivoted_chars)
calculated_ids = apply_calculations_to_ids(non_integer_ids)
combined_integer_ids = get_combined_integer_ids(df_pivoted_chars)
found_combined_integers = lookup_combined_integers(calculated_ids, combined_integer_ids)
print(sum(found_combined_integers))
