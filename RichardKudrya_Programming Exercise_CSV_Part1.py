# The program allows the user to input a number of students, the student first and last name,
# and their three exam scores which the program then stores the data in a CSV File as well as
# displaying all the data in a clean table


import csv

# Constant for CSV file
CSV_FILE = "grades.csv"

# Asks the user for the student data and puts it into a CSV file
def write_grades_to_csv():

    # Asks user to input number of names
    num_students = int(input("Enter the number of students: "))

    # Opens and writes into CSV File
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)

        # Writes the header row
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Loops through each student asking the user a number of questions
        for i in range(num_students):
            print(f"\nData for Student #{i + 1}")

            # Asks for the students name
            first_name = input("Enter the First name of the Student: ").strip()
            last_name = input("Enter the Last name of the student: ").strip()

            # Asks the user for the students grades
            exam1 = int(input("Exam 1 grade: "))
            exam2 = int(input("Exam 2 grade: "))
            exam3 = int(input("Exam 3 grade: "))

            # Writes the data into the CSF File
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    # Tells user data was saved to CSV File
    print(f"\nAll Data has been saved to '{CSV_FILE}'.")


# Runs the function
if __name__ == "__main__":
    write_grades_to_csv()
