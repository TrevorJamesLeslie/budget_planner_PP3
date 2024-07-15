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


def catch_month():
    """
    Function to catch month that user wants to interact with
    """
    global new_month
    while True:
        clear_screen()
        print('WHAT MONTH YOU ARE INTERESTED IN?\n')
        print('TYPE FIRST 3 LETTERS ONLY')
        print(('e.g.: "Jan" for January\n'))
        user_input = input().strip().capitalize()
        new_month = month_abbr.get(user_input)

        if new_month in existing_months:
            break
        elif new_month in full_months and new_month not in existing_months:
            print(f'{new_month} HAS NO CURRENT RECORD')
            print("WHAT WOULD YOU LIKE TO DO INSTEAD ?\n")
            print("1. Generate new month")
            print("2. Go back to main menu \n")
            print("Press ENTER to try again")

            choice = input().strip()
            if choice == '1':
                generate_month()
                break
            elif choice == '2':
                main()
                break
            elif choice == '':
                continue
        else:
            print('Invalid data. Please try again')


def exit_program():
    """
    Function to exit the program
    """
    clear_screen()
    print ("Exiting the program")
    print ("See you next time!\n")
    print("GOODBYE")
    exit()


def budget_decision():
    """
    Prompt user for the next step when previous function was completed
    """    
    while True:
        print('HOPE YOU ARE HAPPY WITH WHAT YOU SEE.' )
        print('WHAT WOULD YOU LIKE TO DO NOW?\n')
        print('1. Go BACK to Main Menu.')
        print(f'2. Show {new_month} budget breakdown\n3. EXIT\n')
        try:
            choice = int(input('Enter your choice here:\n').strip())
            print("\n")
            if choice == 1:
                main()
                break
            if choice == 2:
                display_data()
                break
            elif choice == 3:
                exit_program()
                break
            else:
                clear_screen()
                print('Number out of range.\n')
                print('Please enter a number from the list provided:\n')
                input("Press Enter to continue...\n")
        except ValueError:
            clear_screen()
            print('Invalid data. Please enter a number from the list.\n')
            input("Press Enter to continue...\n")


def income_categories(new_month):
    """
    Add income from listed categories or create new one
    """
    clear_screen()
    while True:
        print(f"CHOOSE AN INCOME OPTION FOR{new_month.upper()}:\n")
        print("For quick income addition, select:")
        print("1. Salary")
        print("2. Sales")
        print("\nFor other actions, select:")
        print("3. Create additional Income ")
        print("4. Go to outgoings")
        print("5. Go back to main menu\n")
        try:
            choice = int(input('Enter Your Choice (1-5): \n').strip())
            if choice in [1, 2]:
                category = "Salary" if choice == 1 else "Sales"
                while True:
                    clear_screen()
                    try:
                        income = int(input(f"ENTER YOUR {category.upper()} INCOME: ").strip())
                        break  # break the loop once input is a number 
                    except ValueError:
                        print('\n')
                        print("Income value must be a digit.\n" )
                        print("Please try again.\n" )
                        input("Press ENTER to continue... ")
                        clear_screen()

                tracker.append_row([new_month, category, income, ''])
                data.setdefault(new_month, {
                        'Category': [], 'Income': [],
                        'Outgoings': []})
                data[new_month]['Category'].append(category)
                data[new_month]['Income'].append(income)
                print(f'Amount of €{income:.2f} was added sucessfully to the {new_month} income.\n')
                print("\n")
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
                clear_screen()
                print('Number out of range.\n')
                print('Please enter a number from the list provided:\n')
                input("Press Enter to continue...\n")
        except ValueError:
            clear_screen()
            print('Invalid data. Please enter a number from the list.\n')
            input("Press Enter to continue...\n")


def add_income(new_month):
    """
    Append income data to the existing month
    """
    clear_screen()
    while True:
        print(f"ADDING {new_month} INCOME:\n")
        print("TYPE NAME AND THE AMOUNT (e.g.: 'cash, 2000'): ")
        print('*NOTE: amount must be a DIGIT\n')
        try:
            user_input = input().strip()
            if ',' in user_input:
                category, income = user_input.split(',')
                category = category.strip()
                income = income.strip()
                # make sure that input is a digit
                if not income.isdigit():
                    raise ValueError("Income amount must be a digit.")

                income = int(income)

                tracker.append_row([
                    new_month, category.capitalize(), income, ''
                ])

                # Create a key:value dict where key is not changing
                data.setdefault(new_month, {
                    'Category': [], 'Income': [],
                    'Outgoings': []
                })
                data[new_month]['Category'].append(category)
                data[new_month]['Income'].append(income)
                print(f'{category.upper()}: €{income:.2f} was added successfully to the {new_month} income.\n')
            else:
                raise ValueError("Invalid input format.")
        except ValueError as e:
            print(f'Error: {e}')
            input("Press ENTER to continue... ")
            clear_screen()
            continue
        print('Press ENTER To Continue Adding...\n')

        print("WHERE WOULD YOU LIKE TO GO NOW?\n")
        print("1. Outgoings")
        print("2. Budget Summary")
        print("3. Main Menu\n")

        

        choice = input('Enter your choice here:\n').strip()
        
        if choice == '1':
            outgoings_categories(new_month)
            break
        elif choice == '2':
            budget_summary(new_month)
            break
        elif choice == '3':
            main()
            break

def outgoings_categories(new_month):
    """
    Add outgoings from listed categories or create new one.
    """
    # create list of outgoings to chose from
    outgoings_list = [
        'House Bills', 'School', 'Creche', 'Shopping', 'Cars', 'Health',
        'Entertainment', 'Holidays', 'ADD NEW'
    ]

    while True:
        clear_screen()
        print(f'CHOOSE OUTGOINGS CATEGORY YOU WANT TO ADD TO :{new_month}')
        print("For quick outgoings addition, select:")
        for i, category in enumerate(outgoings_list, 1):
            print(f'{i}. {category}')
        print("\n To go back to the main menu, select:")
        print('10. Main Main\n')

        try:
            choice = int(input('Please Enter Your Choice: ').strip())
            if choice >= 1 and choice <=8:
                category = outgoings_list[choice - 1]
                print(f"What is your OUTGOINGS amount for {category.upper()}")
                outgoings = int(input().strip())
                tracker.append_row([new_month, category, '', outgoings])
                data.setdefault(new_month, {
                        'Category': [], 'Income': [], 'Outgoings': []})
                data[new_month]['Category'].append(category)
                data[new_month]['Outgoings'].append(outgoings)
                clear_screen()
                print(f'€{outgoings:.2f} was added sucessfully to the {new_month} outgoings.')
                continue
            elif choice == 9:
                add_outgoings(new_month)
                break
            elif choice == 10:
                main()
                break
            elif choice == '':
                continue
            else:
                clear_screen()
                print('Number out of range.\n')
                print('Please enter a number from the list provided:\n')
                input("Press Enter to continue...\n")
        except ValueError:
            clear_screen()
            print('Invalid data. Please enter a number from the list.\n')
            input("Press Enter to continue...\n")


def add_outgoings(new_month):
    """
    Append outgoings data to the existing month.
    """
    while True:
        clear_screen()
        try:
            print(f"ADDING {new_month} OUTGOINGS:\n")
            print("TYPE NAME AND THE AMOUNT (e.g.: 'clothes, 200'): ")
            print('*Note. Amount must be a DIGIT\n')
            category, outgoings = input().split(',').strip()
            tracker.append_row([
                    new_month, category.strip().capitalize(),
                    int(outgoings.strip()), ''])
            # create a key :value dict where key is not changing
            data.setdefault(new_month, {
                    'Category': [], 'Income': [], 'Outgoings': []})
            data[new_month]['Category'].append(category)
            data[new_month]['Outgoings'].append(int(outgoings))

            clear_screen()
            print(f"Added {outgoings} to {category.upper} for {new_month}.\n")
        except ValueError:
            print('Invalid input format')
            print('Please use format: name, amount(number only). \n')

        print("Press ENTER To Continue, or Chose From Options Below: \n")
        print("1. Go To Budget Summary")
        print("2. Go Back to Main Menu\n")
        
        choice = input('Enter your choice here:\n').strip()
        choice = input().strip()
        if choice == '1':
            budget_summary(new_month)
            break
        elif choice == '2':
            main()
            break
        elif choice == '':
            continue


def generate_month():
    """
    Confirm whether or not month exists in the tracking list.
    If not, generate a new one and append to the list.
    """
    global new_month
    while True:
        clear_screen()
        print("LET'S CREATE A NEW MONTH \n")
        print('TYPE FIRST 3 LETTERS OF THE MONTH:\n')
        print(" 'Jan' for January, 'Feb' for February etc.\n")
        try:
            user_input = input().strip().capitalize()
            new_month = month_abbr.get(user_input)
            clear_screen()
            if new_month:
                if new_month in existing_months:
                    print(f'Oopsi...{new_month} already EXISTS.')
                    print('What would you like to do? \n')
                    print('1. Add Income or Outgoings to this month')
                    print('2. Go back to Main Menu')
                    print('3. Generate new month\n')
                    print('Please enter your choice: ')
                    choice = (input().strip())
                    if choice == '1':
                        choose_category(new_month)
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
                    choose_category(new_month)
                    break
            else:
                clear_screen()
                print(f'"{user_input}" Does not match the criteria.\n')
                print("Please Try Again.\n")
                input("Press Enter to continue...\n")
        except ValueError:
            clear_screen()
            print("Oops, somtheing went wrong. Please try again.\n")
            input("Press Enter to continue...\n")


def choose_category(new_month):
    """
    Let user chose whatever category (income or outcome).
    """
    while True:
        clear_screen()
        print(f'What would you like to do now with {new_month} ?\n')
        print('1. Add Income\n2. Add Outgoings\n3. EXIT\n')
        try:
            choice = int(input('Please Enter Your Choice: \n').strip())
            if choice == 1:
                income_categories(new_month)
                break
            elif choice == 2:
                outgoings_categories(new_month)
                break
            elif choice == 3:
                exit_program()
                break
            else:
                clear_screen()
                print('Number out of range.\n')
                print('Please enter a number from the list provided:\n')
                input("Press Enter to continue...\n")
        except ValueError:
            clear_screen()
            print('Invalid data. Please enter a number from the list.\n')
            input("Press Enter to continue...\n")


def budget_summary(new_month):
    """
    Filter through the data and display only one with corresponding month.
    """
    clear_screen()
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

    balance = total_income - total_outgoings
    # Append totals to the 'summary' worksheet
    summary.append_row([new_month, total_income, total_outgoings, balance])
    summary_data = {
        "Month": [new_month], "Total income": [total_income],
        "Total outgoings": [total_outgoings], "balance": [balance]
    }
    if not month_rows:
        print(f"No data available for {new_month}.")
    else:
        print(f"Budget Summary for {new_month}")
        print(f"Total Income: €{total_income:.2f}")  # convert amount into float  
        print(f"Total Outgoings: €{total_outgoings:.2f}")
        print(f"Balance: €{balance:.2f}\n")
        

def display_data():
    """
    Display budget detailed data to the user.
    """
    clear_screen()
    global new_month
    # display the data so that it can be acessed and deleted
    all_values = tracker.get_all_values()
    if not all_values:
        print("Data is not availabe")
        return
    # skip the header row (first row)
    data_rows = all_values[1:]

    # design the table
    print("-" * 60) 
    print(
        f"{'Index':<7}{'Month':<10}{'Category':<20}"
        f"{'Income':<10}{'Outgoings':<10}")
    print("-" * 60)
    
    for index, row in enumerate(data_rows, start=1):
        month = row[0]
        category = row[1]
        income = row[2] if row[2] else '0'
        outgoings = row[3] if row[3] else '0'
        print(
            f'{index:<7}{month:<10}{category:<20}'
            f'{income:<10}{outgoings:<10}')


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
                    "What line number you wish to delete?\n***Press 'X' Exit ").strip())
            if index_to_delete > 0 and index_to_delete < len(all_values):
                tracker.delete_rows(index_to_delete + 1)  # +1indices start at1
                print(f'Entry at line {
                        index_to_delete} has been deleted sucesfully')
                continue
            else:
                choice = input().strip().lower
                if choice == "x":
                    main()
                else:
                    clear_screen()
                    print("Invalid index. Please enter number within the range.")
        except ValueError:
            clear_screen()
            print("invalid input. Please enter a number.")

def welcome_page():
    """
    Display welcome message to the user with options to choose from for the next step.
    """
    print("\n")
    print('$$$ WELCOME TO BUDGET TRACKER $$$\n')
    print('WOULD YOU LIKE TO GET CLEAR ON WHERE YOUR MONEY GOES?\n')
    print("LET'S GET STARTED THEN!\n")
    print('\n')
    input("Press ENTER to begin... ")  


def main():
    """
    Display main menu to the user with the core functions
    """
    while True:
        clear_screen()
        print('Please choose from the following options: \n')
        print('1. Display budget summary')
        print('2. Generate budget')
        print("3. Add data to the existing month ")
        print('4. Delete entry')
        print('5. EXIT\n')
        try:
            choice = int(input('Choice: 1, 2, 3, 4. Please Enter Number: \n').strip())
            print("\n")
            if choice == 1:
                catch_month()
                budget_summary(new_month)
                budget_decision()
                break
            elif choice == 2:
                clear_screen()
                generate_month()
                break
            elif choice == 3:
                catch_month()
                choose_category(new_month)
                break
            elif choice == 4:
                catch_month()
                delete_entry(new_month)
                break
            elif choice == 5:
                clear_screen()
                exit_program()
                break
            else:
                clear_screen()
                print('Number out of range.\n')
                print('Please enter a number from the list provided:\n')
                input("Press Enter to continue...\n")
        except ValueError:
            clear_screen()
            print('Invalid data. Please enter a number from the list.\n')
            input("Press Enter to continue...\n")


# calling the main function
welcome_page()
main()