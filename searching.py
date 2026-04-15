from pathlib import Path
import json
import time

import matplotlib.pyplot as plt
from generators import unordered_sequence, ordered_sequence


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """

    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name


    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if field in data.keys():
        return data[field]
    else:
        return None

def linear_search(searched_data, searched_number):
    slovnik = {}
    seznam_dvojic = []
    count = 0
    for i, value in enumerate(searched_data):
        if searched_number == value:
            count += 1
            seznam_dvojic.append(i)

    slovnik["positions"] = seznam_dvojic
    slovnik["count"] = count
    return slovnik

def binary_search(searched_data, searched_number):
    left = 0
    right = len(searched_data) - 1

    while left <= right:


        mid = (left + right) // 2
        prostredni_cislo = searched_data[mid]

        if prostredni_cislo == searched_number:
            return mid
        elif prostredni_cislo < searched_number:
            left = mid + 1
        elif prostredni_cislo > searched_number:
            right = mid - 1
    return None



def test_complexity(list_of_n):
    number = 42
    times_linear = []
    times_binary = []
    for n in list_of_n:
        unordered_data = ordered_sequence(n)

def pattern_search(sequenci, pattern):
    indices = {}
    return indices







def main():
    my_data = read_data("sequential.json", "ordered_numbers")
    print(my_data)

    data = linear_search(my_data, 0)
    print(data)
    duration = 0
    rep = 100
    for measurements in range(100):
        start_time_linear = time.perf_counter()
        found_num = linear_search(my_data, 0)
        end_time_time_linear = time.perf_counter()
        duration += end_time_time_linear - start_time_linear
    print(duration)
    ukol3 = binary_search(my_data, -1)
    print(ukol3)


if __name__ == "__main__":
    main()
