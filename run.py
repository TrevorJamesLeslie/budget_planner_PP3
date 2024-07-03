import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
# const for security file not to be tracked
CREDS = Credentials.from_service_account_file('creds.json')
# const for credentials scoped
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# const to allow auth of gspread client within these scoped credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
# const to open spread sheet
SHEET = GSPREAD_CLIENT.open('budget_planner')


tracker = SHEET.worksheet('tracker')
data = tracker.get_all_values()


def main():
    """
    Welcome Message to the user with options to chose from for the next step.
    """

    print('*** WELCOME TO BUDGET TRACKER ***\n')
    print('Would you like to get clear on where your money goes?')
    print("Let's get started!")
    print('Please choose from the following options: \n')
    print('1. Display Budget Summary\n')
    print('2. Generate Budget\n')
    print('3. Edit Budget\n')

    # loop throught the choices
    # Source : Python Exception Handling(CI)
    while True:
        try:
            choice = int(input('Please Enter Your Choice Here :'))
            if choice == 1:
                display_summary()
                break
            elif choice == 2:
                add_category()
                break
            elif choice == 3:
                edit_budget()
                break
            else:
                print('Number Out Of Range.\n')
                print('PleaseEnter Number From The List Provided.\n')
        except ValueError:
            print('Invalid Data. Please Enter Number From The List.\n')
            continue


# pull all the values from the first column(index1)
month_data = tracker.col_values(1)
# since first row is a header, skip it
existing_months = month_data[1:]  # columns are 1 based not 0

# create full month list
full_months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Create a dictionary for month abbreviations
# only first 3 letters needed, making it easy for the user
month_abbr = {month[:3].capitalize(): month for month in full_months}


def add_category():
    """
    Confirm weather or not month exists in the tracking list
    """
    print('Please Type First 3 letters Of The Month You Wish To Add:')
    while True:
        try:
            user_input = input().strip().capitalize()
            if user_input in month_abbr and user_input in existing_months:
                print('This month already exists.)
                print('Please add a new month)
                print('to VIEW or EDIT current months press x')
                if user_input == 'x' or 'X':
                    main()
                break
            if user_input in month_abbr and user_input not in existing_months:
                full_month_name = month_abbr[user_input]
                print(f"Creating new month: {full_month_name}")
                # append month to the google sheet tracker
                tracker.append_row([full_month_name])
                print(f"{full_month_name} has been added sucessfully")
                # chose_category()
                break
            else:
                print(f"{user_input} does not match criteria: ")
                print('type first 3 letters only')
        except ValueError:
            print('Invalid Data. Please Enter Number From The List.\n')
            continue

# calling the main function


main()