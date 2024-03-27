import json
import csv

def read_json_file(json_file_path):
    """Reads a JSON file and returns the data."""
    with open(json_file_path, 'r') as file:
        return json.load(file)

def convert_json_to_csv(json_data, csv_file_path):
    """Converts JSON data to CSV format and writes it to a file."""
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = json_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in json_data:
            writer.writerow(data)

if __name__ == "__main__":
    print("Please type the filepath to the JSON and press enter:")
    json_file_path = input().strip()

    print("Now, type the full file path and filename of the output CSV (e.g., c:\\output.csv):")
    csv_file_path = input().strip()

    print("converting...")

    # Read the JSON data
    json_data = read_json_file(json_file_path)

    # Convert and write the JSON data to a CSV file
    convert_json_to_csv(json_data, csv_file_path)

    print("converted!")
    input("Press any key to exit...")
