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
all_values = tracker.get_all_values()




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
data= {}



def add_income(new_month):

    """
    Append income data to the existing month

    """
    while True:
        category, income = input("Type in income name and amount (e.g : salary, 2000): "
                ).split(',')
        tracker.append_row([new_month, category, income, ', '])
        data[new_month]['category'].append(category)
        data[new_month]['income'].append(income)
        print(f"Added {income} to {category} for {new_month}.")
        
        decision = input("Type 'x' if you are done adding the income\n")
        if decision.lower() == "x":
            break



def chose_category(new_month):
    """
    Let user chose what wether category is income or outcome
    """
    while True:
        print('What Category You Are Interested In?')
        print('Choose From Options Below')
        print('Please chose your category(type in number only: 1 or 2): \n')
        print('1. Income \n')
        print('2. Outgoings \n')


        try:
            choice = int(input('Please Enter Your Choice Here: '))
            if choice == 1:
                add_income(new_month)
                break
            elif choice == 2:
                category, outgoings = input(
                        "Type outgoings name and amount(e.g., shop, 150): "
                        ).split(',')
                add_outgoings(new_month, category, outgoings)
                break
            else:
                print('Number Out Of Range.\n')
                print('Please Enter Number From The List Provided:\n')
                continue
        except ValueError:
            print('Invalid Data. Please Enter Number From The List.\n')




def generate_month():
    """
    Confirm weather or not month exists in the tracking list.
    If not generate new one and append tothe lsit
    """
    print('Please Type First 3 letters Of The Month You Wish To Add:')
    while True:
        try:
            user_input = input().strip().capitalize()
            full_month_name = month_abbr.get(user_input)
            if full_month_name:
                if full_month_name in existing_months:
                    print(f'{full_month_name} Already Exists')
                    print('Please Add A New Month')
                    continue
               
                else:
                    print(f"Creating new month: {full_month_name}")
                    # append month to the google sheet tracker
                    tracker.append_row([full_month_name])
                    existing_months.append(full_month_name)
                    data[full_month_name] = {
                            "category": [], "income": [], "outgoings": []}
                    print(f"{full_month_name} has been added sucessfully")
                    chose_category(full_month_name)
                break
            else:
                print(f"{user_input} does not match the criteria: \n")
        except ValueError:
            print('Invalid Data.\n')
        continue




def main():
    """
    Welcome Message to the user with options to chose from for the next step.
    """


    print('*** WELCOME TO BUDGET TRACKER ***\n')
    print('Would you like to get clear on where your money goes?\n')
    print("Let's get started!\n")


    # loop throught the choices2
    # Source : Python Exception Handling(CI)
    while True:
        print('Please choose from the following options: \n')
        print('1. Display Budget Summary\n')
        print('2. Generate Budget\n')
        print('3. Edit Budget\n')
        try:
            choice = int(input('Please Enter Your Choice ( 1, 2 or 3) Here: '))
            if choice == 1:
                display_summary()
                break
            elif choice == 2:
                generate_month()
                break
            elif choice == 3:
                edit_budget()
                break
            else:
                print('Number Out Of Range.\n')
                print('Please Enter Number From The List Provided:\n')
        except ValueError:
            print('Invalid Data. Please Enter Number From The List.\n')
            continue




# calling the main function
main()



