import os
import csv
import json

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for key, value in row.items():
                if not key in data:
                    data[key] = []
                data[key].append(value)
    return data


def selection_sort(data):
    index = 0
    data_1 = data["series_1"]
    while index < len(data_1):
        smallest = min(data_1[index:])
        for i, number in enumerate(data_1[index:]):
            if number == smallest:
                idx = i
                data_1[index], data_1[idx+index] = data_1[idx+index], data_1[index]
                break
        index += 1
    return data_1

def main():
    data = read_data("numbers.csv")
    print(selection_sort(data))


if __name__ == '__main__':
    main()
