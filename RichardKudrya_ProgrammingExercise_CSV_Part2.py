# This program will read the data in the CSV File and displays the data in tabular format


import csv

# Constant for CSV File
CSV_FILE = "grades.csv"

# Reads the data from the CSV file and displays it
def read_and_display_grades():

    print("\nGrades Report\n")

    # Use the 'with' keyword to safely open the file
    with open(CSV_FILE, mode="r", newline="") as file:
        reader = csv.reader(file)

        header = next(reader)

        # Prints the header
        print(f"{header[0]:<15}{header[1]:<15}{header[2]:<10}{header[3]:<10}{header[4]:<10}")
        print("-" * 60)

        # Prints the data in tabular format
        for row in reader:
            print(f"{row[0]:<15}{row[1]:<15}{row[2]:<10}{row[3]:<10}{row[4]:<10}")

    print("\nEnd of report.\n")


# Runs the function
if __name__ == "__main__":
    read_and_display_grades()
