# Python Typing Text Effect
# Credits: 101computing.net/python-typing-text-effect/
import os
import gspread
from google.oauth2.service_account import Credentials

# Constants for google sheets API
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


# Security file not to be tracked
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
# Authorize of gspread client within these scoped credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('budget_planner')


tracker = SHEET.worksheet('tracker')
summary = SHEET.worksheet('summary')

full_months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
# this line was created with help of chat GPT
# only first 3 letters needed, making it easy for the user
month_abbr = {month[:3].capitalize(): month for month in full_months}


# since first row is a header, skip it
existing_months = tracker.col_values(1)[1:]  # columns are 1 based not 0
# set new_month as global variable to acess throughout the code
data = {}
new_month = ""


# Tutorial:https://www.101computing.net/python-typing-text-effect/
def clear_screen():
    """
    Clear screen function for CLI
    """
    os.system("clear")

##############################################################################
def catch_month():
    """
    Function to catch month that user wants to interact with
    """
    global new_month
    while True:
        clear_screen()
        print('TYPE FIRST 3 LETTERS OF THE MONTH YOU ARE INTERESTED IN? \n')
        print(('sep" for "September" \n'))
        try:
            user_input = input().strip().capitalize()
            new_month = month_abbr.get(user_input)

            if new_month in existing_months:
                break
            elif new_month in full_months and new_month not in existing_months:

                print(f'{new_month} Have No Current Record')
                print("What Would You Like To Do ? \n")
                print("1. Generate New Month")
                print("2. Go Back To Main Menu \n")
                print("Press ENTER to Try Again")

                choice = input().strip()
                if choice == '1':
                    generate_month()
                    break
                elif choice == '2':
                    main()
                    break
                elif choice == '':
                    continue
        except ValueError:
            print('Invalid Data. Please try again')


def budget_decision():
    global new_month

    while True:
        print('Question:  "What would you like to do now? \n')
        print('1. Display Budget Summary \n')
        print('2. Edit Current Budget \n')
        print('3. EXIT \n')
        try:
            choice = int(input('Enter Your Choice (1, 2 or 3) Here: \n').strip())
            print("\n")
            if choice == 1:
                budget_summary(new_month)
                break
            elif choice == 2:
                add_income(new_month)
                break
            elif choice == 3:
                print("Exiing the program")
                break
            else:
                print('Number Out Of Range. Please Enter a Valid Number.\n')
        except ValueError:
            print('Invalid Data. Please Enter a Valid Number.\n')


def income_categories(new_month):
    """
    User can chose from list of categories to add income
    """
    clear_screen()
    while True:
        print(f'CHOSE INCOME OPTION FOR MONTH: {new_month}')
        print('Number value only: 1, 2, 3, 4, 5): \n')
        print('1. Salary')
        print('2. Sales')
        print('3. Add New Income\n')
        print('4. Skip to Outgoings')
        print('5. Go Back To Main Menu \n')
        try:
            choice = int(input('Please Enter Your Choice: ').strip())
            if choice in [1, 2]:
                category = "Salary" if choice == 1 else "Sales"
                while True:
                    try:
                        income = int(input(f"What is Your INCOME from {category.upper()}: \n").strip())
                        break  # break the loop once input is an int 
                    except ValueError:
                        print('\n')
                        print(" Income value must be must be a digit.\n" )
                        print(" Please Try Again.\n" )
                        input("Press Enter to continue...")
                        clear_screen()

                tracker.append_row([new_month, category, income, ''])
                data.setdefault(new_month, {
                        'Category': [], 'Income': [],
                        'Outgoings': []})
                data[new_month]['Category'].append(category)
                data[new_month]['Income'].append(income)
                print(f'Income of {income} added sucessfully to the {new_month} budget')
                clear_screen()
                continue
            elif choice == 3:
                add_income(new_month)
                break
            elif choice == 4:
                outgoings_categories(new_month)
                break
            elif choice == 5:
                main()
                break
            else:
                print('Number Out Of Range.\n')
                print('Please Enter Number From The List Provided:\n')
                input("Press Enter to continue...")  # Pause to let user read the message
                clear_screen()
        except ValueError:
            print('Invalid Data. Please Enter Number From The List.\n')
            input("Press Enter to continue...")  # Pause to let user read the message
            clear_screen()

def add_income(new_month):

    """
    Append income data to the existing month
    """
    while True:
        clear_screen()
        try:
            print(f"{new_month} INCOME:\n")
            print("TYPE NAME AND THE AMOUNT ( *cash, 2000): ")
            print('* NOTE: AMOUNT MUST BE A DIGIT\n')
            category, income = input().split(',')
            tracker.append_row([
                    new_month, category.strip().capitalize(),
                    int(income.strip()), ''])

            # create a key :value dict where key is not changing
            data.setdefault(new_month, {
                    'Category': [], 'Income': [],
                    'Outgoings': []})
            data[new_month]['Category'].append(category)
            data[new_month]['Income'].append(int(income))

            clear_screen()
            print(f"Added {income} to {category} for {new_month}.\n")
        except ValueError:
            print('Invalid input')
            print('Please use format: name, amount(number only).\n')

        print("Press ENTER To Continue, or Chose From Option Below: \n")
        print("1. Outgoings ")
        print("2. Budget Summary\n")

        print('Enter Your Choice Here (1,2 or ENTER): ')
        choice = input().strip()
        if choice == '1':
            outgoings_categories(new_month)
            break
        elif choice == '2':
            budget_summary()
            break
        elif choice == '':
            continue


def outgoings_categories(new_month):

    """
   List of categories to chose from in outgoings
    """
    # create list of outgoings to chose from
    outgoings_list = [
        'House Bills', 'School', 'Creche', 'Shopping', 'Cars', 'Health',
        'Entertainment', 'Holidays', 'ADD NEW'
        ]

    while True:
        clear_screen()
        print(f'What OUTGOINGS Are You Interested In for {new_month} ? ')
        print('Number Value between 1 - 10 only): \n')
        for i, category in enumerate(outgoings_list, 1):
            print(f'{i}. {category}')

        print('11. Main Menu \n')

        try:
            choice = int(input('Please Enter Your Choice Here: \n').strip())
            if choice >= 1 and choice <= 9:
                category = outgoings_list[choice - 1]
                print(f"What is Your OUTGOINGS Amount for {category.upper()}")
                outgoings = int(input().strip())
                tracker.append_row([new_month, category, '', outgoings])
                data.setdefault(new_month, {
                        'Category': [], 'Income': [], 'Outgoings': []})
                data[new_month]['Category'].append(category)
                data[new_month]['Outgoings'].append(outgoings)
                continue

            elif choice == 2:
                category = "Sales"
                print("What is Your INCOME from SALES : ")
                income = int(input().strip())
                tracker.append_row([new_month, category, income, ''])
                data.setdefault(new_month, {
                        'Category': [], 'Income': [], 'Outgoings': []})
                data[new_month]['Category'].append(category)
                data[new_month]['Income'].append(income)
                continue
            elif choice == 11:
                main()
                break
            elif choice == '':
                continue
            else:
                print('Number Out Of Range.\n')
                print('Please Enter Number From The List Provided:\n')
        except ValueError:
            print('Invalid Data. Please Enter Number From The List.\n')


def add_outgoings(new_month):

    """
    Append outgoings data to the existing month
    """
    while True:
        clear_screen()
        try:
            print(f"{new_month} OUTGOINGS:")
            print("Type in name and amount(e.g.: Shop, 2000): \n")
            print('*Please ensure that amount has a number value\n')
            category, outgoings = input().split(',')
            tracker.append_row([
                    new_month, category.strip().capitalize(),
                    int(outgoings.strip()), ''])
            # create a key :value dict where key is not changing
            data.setdefault(new_month, {
                    'Category': [], 'Income': [], 'Outgoings': []})
            data[new_month]['Category'].append(category)
            data[new_month]['Outgoings'].append(int(outgoings))

            clear_screen()
            print(f"Added {outgoings} to {category} for {new_month}.\n")
        except ValueError:
            print('Invalid input format')
            print('Please use format: name, amount(number only). \n')

        print("Press ENTER To Continue, or Chose From Options Below: \n")
        print("1. Go To Budget Summary")
        print("2. Go Back to Main Menu\n")
        print('Enter Your Choice Here (1,2 or ENTER): ')
        choice = input().strip()
        if choice == '1':
            budget_summary()
            break
        elif choice == '2':
            main()
            break
        elif choice == '':
            continue


def generate_month():
    """
    Confirm weather or not month exists in the tracking list.
    If not generate new one and append tothe lsit
    """

    global new_month
    while True:
        print("LET'S CREATE A NEW MONTH \n")
        print('TYPE FIRST 3 LETTERS OF THE MONTH:\n')
        print(" * 'jan' for January, 'feb' for February etc.* \n")
        try:
            user_input = input().strip().capitalize()
            new_month = month_abbr.get(user_input)
            clear_screen()
            if new_month:
                if new_month in existing_months:
                    print(f'Uppsi...{new_month} ALREADY EXISTS.')
                    print('What would you like to do? \n')
                    print('1. EDIT This Month')
                    print('2. GO BACK To Main Menu')
                    print('3. ADD New Month \n')
                    print('Please Enter Your Choice Here: ')
                    choice = (input().strip())
                    if choice == '1':
                        chose_category(new_month)
                        break
                    elif choice == '2':
                        main()
                        break
                    elif choice == '3':
                        continue
                else:
                    print(f"Creating new month: {new_month}")
                    # append month to the google sheet tracker
                    # tracker.append_row([new_month, '', '', ''])
                    # existing_months.append(new_month)
                    data[new_month] = {
                            "Category": [], "Income": [], "Outgoings": []}
                    print(f"{new_month} has been added sucessfully\n")
                    ("\n")
                    chose_category(new_month)
                    break
            else:
                print(f"{user_input} Does not match the criteria.\n")
                print("Please Try Again.\n")
                print("\n")
        except ValueError:
            print('Invalid Data.\n')


def chose_category(new_month):

    """
    Let user chose whatever category (income or outcome).
    """
    clear_screen()
    while True:
        print(f'What Category You Are Interested In for {new_month} ?')
        print('1. Income\n2. Outgoings\n3. EXIT\n')
        try:
            choice = int(input('Please Enter Your Choice: \n').strip())
            if choice == 1:
                income_categories(new_month)
                break
            elif choice == 2:
                outgoings_categories(new_month)
                break
            elif choice == 3:
                print("Exitng the program")
                break
            else:
                print(f"{choice} Does not match the criteria.\n")
                print('Please Enter Number From The List.\n')
        except ValueError:
            print('Invalid Data. Please Enter Number From The List.\n')


def budget_summary(new_month):
    """
    Filter through the data and display only one with coresponding month
    """

    # Pull data from tracker worksheet
    all_values = tracker.get_all_values()

    # List to collect all the data with chosen month
    month_rows = []

    total_income = 0
    total_outgoings = 0

    for row in all_values:
        if row[0] == new_month:
            month_rows.append(row)
            # Append filtered rows to the summary worksheets
            income = int(row[2]) if row[2] else 0
            outgoings = int(row[3]) if row[3] else 0
            total_income += income
            total_outgoings += outgoings

    # Calculate balance
    balance = total_income - total_outgoings

    # Append totals to the 'summary' worksheet
    summary.append_row([new_month, total_income, total_outgoings, balance])
    summary_data = {
            "Month": [new_month], "Total income": [total_income],
            "Total outgoings": [total_outgoings], "balance": [balance]}

    if not month_rows:
        print(f"no data available for {new_month}.")
    else:
        print(
            f'Summary for {new_month}: Total Income: {total_income}, '
            f'Total Outgoings: {total_outgoings}, Balance: {balance} \n')

        print(f"Detailed Data for {new_month}:\n")
        for row in month_rows:
            print(row)
    return summary_data


def display_data():
    """
    Display data to the user
    """
    global new_month
    # display the data so that it can be acessed and deleted
    all_values = tracker.get_all_values()
    if not all_values:
        print("Data is not availabe")
        return

    # design the table
    print(
        f"{'Index': < 5}{'Month': < 10}{'Category': < 20}"
        f"{'Income': < 10}{'Outgoings': < 10}")
    print("_" * 60)

    for index, row in enumerate(all_values):
        month = row[0]
        category = row[1]
        income = row[2] if row[2] else '0'
        outgoings = row[3] if row[3] else '0'
        print(
            f'{index: < 5}{month: < 10}{category: < 20}'
            f'{income: < 10}{outgoings: < 10}')


def delete_entry(new_month):
    """
    Delete data from the tracker worksheet based on user input.
    """
    all_values = tracker.get_all_values()

    if not all_values:
        print("No data available to Delete")
        return

    while True:
        try:
            display_data()
            print("\n")
            index_to_delete = int(input(
                    'What index line you wish to delete? \n').strip())
            if index_to_delete > 0 and index_to_delete < len(all_values):
                tracker.delete_rows(index_to_delete + 1)  # +1indices start at1
                print(f'Entry at index {
                        index_to_delete} has been deleted sucesfully')
                continue
            else:
                print("Invalid index. Please enter number within the range.")
        except ValueError:
            print("invalid input. Please enter a number.")


def main():
    """
    Welcome Message to the user with options to choose from for the next step.
    """
    print('*** WELCOME TO BUDGET TRACKER ***\n')
    print('WOULD YOU LIKE TO GET CLEAR ON WHERE YOUR MONEY GOES?\n')
    print("LET'S GET STARTED THEN!\n")
    input("Press Enter to continue...")  # Pause to let user read the welcome message

    while True:
        clear_screen()
        print('Please choose from the following options: \n')
        print('1. Display Budget Summary')
        print('2. Generate Budget')
        print('3. Edit Budget')
        print('4. EXIT\n')
        try:
            choice = int(input('Choice: 1, 2, 3, 4. Please Enter Number: \n').strip())
            print("\n")
            if choice == 1:
                catch_month()
                budget_summary(new_month)
                break
            elif choice == 2:
                clear_screen()
                generate_month()
                break
            elif choice == 3:
                catch_month()
                chose_category(new_month)
                break
            elif choice == 4:
                clear_screen()
                print("Exiting the program \n")
                print("GOODBYE")
                break
            else:
                print('Number out of range.\n')
                print('Please enter a number from the list provided:\n')
                input("Press Enter to continue...\n")
        except ValueError:
            print('Invalid data. Please enter a number from the list.\n')
            input("Press Enter to continue...\n")

# calling the main function
#main()
income_categories(new_month)