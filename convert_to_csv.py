import pandas as pd
import json
import os
from datetime import datetime

"""
This script converts a JSON file to a CSV file with a unique timestamped filename.

How to run the program:
1. Make sure you have Python installed on your system.
2. Install the Pandas library if you haven't already by running:
   pip install pandas
3. Update the 'json_file_path' and 'csv_file_path' placeholders with the actual file paths.
   Note: Use double backslashes (\\) in the file paths to escape the backslash character in Python strings.
4. Save this script as 'convert_to_csv.py'.
5. Open your command line interface and navigate to the directory where 'convert_to_csv.py' is saved.
6. Run the script by executing:
   python convert_to_csv.py
"""

# Define the file paths
json_file_path = 'path\\to\\your\\json\\file.json'  # Replace with your actual JSON file path
# Note: Use double backslashes (\\) in the file paths to escape the backslash character in Python strings

# Generate a new CSV file path with a timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
csv_file_path = f'path\\to\\your\\csv\\output_{timestamp}.csv'  # Replace with your desired CSV output path
# Note: Use double backslashes (\\) in the file paths to escape the backslash character in Python strings

try:
    # Load the JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Convert the JSON data to a DataFrame
    df = pd.DataFrame(data)

    # Save the DataFrame as a CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"CSV file has been saved to {csv_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
