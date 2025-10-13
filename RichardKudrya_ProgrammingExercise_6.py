# Description:
# This program will validate your social security number, phone number
# and zipcode using regular expressions. The program will ask the user
# for the following three then display whether each is valid or not.


import re


PHONE_PATTERN = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
SSN_PATTERN = r'^\d{3}-\d{2}-\d{4}$'
ZIP_PATTERN = r'^\d{5}(-\d{4})?$'



# This function validates whether the phone number matches the pattern

def validate_phone(phone_number):
    return bool(re.match(PHONE_PATTERN, phone_number))


# This function validates whether the Social Security number matches the pattern

def validate_ssn(ssn):
    return bool(re.match(SSN_PATTERN, ssn))


# This function validates whether the Zip Code matches the pattern

def validate_zip(zip_code):
    return bool(re.match(ZIP_PATTERN, zip_code))


# This function asks the user for each of the inputs, validates each input and displays whether each input is
# valid or not

def main():
    phone_number = input("Enter your phone number (123-456-7890): ")
    ssn = input("Enter your Social Security Number (123-45-6789): ")
    zip_code = input("Enter your ZIP code (12345): ")

    print("\n- Results -")

    if validate_phone(phone_number):
        print("Phone Number is valid")
    else:
        print("Phone Number is invalid")

    if validate_ssn(ssn):
        print("Social Security Number is valid")
    else:
        print("Social Security Number is invalid")

    if validate_zip(zip_code):
        print("ZIP Code is valid")
    else:
        print("ZIP Code is invalid")


# This function runs the program
if __name__ == "__main__":
    main()
