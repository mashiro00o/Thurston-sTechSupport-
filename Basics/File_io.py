import csv
import json

# Function to read a non-delimited file
def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

# Function to write data to a non-delimited file
def write_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

# Function to read a CSV file
def read_csv(filename):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

# Function to write data to a CSV file
def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Function to read a JSON file
def read_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Function to write data to a JSON file
def write_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Example usage:

# Read non-delimited file
non_delimited_data = read_file('non_delimited.txt')

# Write to non-delimited file
write_file('output_non_delimited.txt', non_delimited_data)

# Read CSV file
csv_data = read_csv('data.csv')

# Write to CSV file
write_csv('output.csv', csv_data)

# Read JSON file
json_data = read_json('data.json')

# Write to JSON file
write_json('output.json', json_data)
