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
column = tracker.col_values(1)

summary = SHEET.worksheet('summary')
summary_values = summary.get_all_values()




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
#set new_month as global variable to acess throughout the code 
new_month = ""

data= {}




def budget_decision():
    """ 
    Display 3 options to the user with chocie to make after budget data is enetered.
    Decision to make a choice between viewing summary, view details ,editing 
    """
    global new_month

    while True:
        print('Question:  "What would you like to do now? \n')
        print('1. Display Budget Summary \n')
        print('2. Edit Current Budget \n')
        print('3. EXIT \n')
        try:
            choice = int(input('Enter Your Choice ( 1, 2 or 3) Here:  '))
            print("\n")
            if choice == 1:
                budget_summary(new_month)
                break
            elif choice == 2:
                add_income(new_month)
                break
            elif choice == 3:
                main()
                break
            else:
                print('Number Out Of Range.\n')
                print('Please Enter Number From The List Provided:\n')
        except ValueError:
            print('Invalid Data. Please Enter Number From The List.\n')
            continue

 
def add_income(new_month):

    """
    Append income data to the existing month

    """
    while True:
        category, income = input("INCOME: Type in name and amount (e.g.: salary, 2000): "
                ).split(',') 
        tracker.append_row([new_month, category, income, '  '])
        data[new_month]['category'].append(category)
        data[new_month]['income'].append(income)
        print(f"Added {income} to {category} for {new_month}.\n")
        

        decision = input("Type 'x' if you are done adding the income\n")
        if decision.lower() == "x":
            add_outgoings(new_month)
            break

def add_outgoings(new_month):

    """
    Append income data to the existing month

    """
    while True:
        category, outgoings = input("OUTGOINGS: Type in name and amount (e.g.: shop, 2000): "
                ).split(',')
        tracker.append_row([new_month, category, '  ', outgoings])
        data[new_month]['category'].append(category)
        data[new_month]['income'].append(outgoings)
        print(f"Added {outgoings} to {category} for {new_month}.\n")
        
        decision = input("Type 'x' + 'ENTER' if you are done adding outgoings \n")
        if decision.lower() == "x":
            budget_decision()
            break


def chose_category(new_month):
    """
    Let user chose what wether category is income or outcome
    """
    while True:
        print('What Category You Are Interested In? ')
        print('Choose From Options Below\n')
        print('Please chose your category(type in number only: 1 or 2): \n')
        print('1. Income \n')
        print('2. Outgoings \n')


        try:
            choice = int(input('Please Enter Your Choice Here: '))
            if choice == 1:
                add_income(new_month)
                break
            elif choice == 2:
                add_outgoings(new_month)
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
    global new_month

    print('Please Type First 3 letters Of The Month You Wish To Add:')
    while True:
        try:
            user_input = input().strip().capitalize()
            new_month = month_abbr.get(user_input)
            if new_month:
                if new_month in existing_months:
                    print(f'{new_month} Already Exists')
                    print('Please Add A New Month or :')
                    print("1. Type 'e' and pess 'ENTER' to EDIT the month \n")
                    print("2. Type 'x' and press 'ENTER' to EXIT \n")
                    decision = input()
                    if decision.lower() == 'e':
                        chose_category(new_month)
                    elif decision.lower() == 'x':
                        main()
                        break
               
                else:
                    print(f"Creating new month: {new_month}")
                    # append month to the google sheet tracker
                    #tracker.append_row([new_month, '', '', ''])
                    #existing_months.append(new_month)
                    data[new_month] = {
                            "category": [], "income": [], "outgoings": []}
                    print(f"{new_month} has been added sucessfully\n")
                    ("\n")
                    chose_category(new_month)
                break
            else:
                print(f"{user_input} does not match the criteria: \n")
        except ValueError:
            print('Invalid Data.\n')
        continue


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
    balance = 0

    for row in all_values:
        if row [0] == new_month:
            month_rows.append(row)

    # Append filtered rows to the summary worksheets
    for row in month_rows:
        income = int(row[2]) if row[2] else 0
        outgoings = int(row[4]) if row[4] else 0

    total_income += income
    total_outgoings += outgoings

    # Calculate balance
    balance = total_income - total_outgoings

    # Append totals to the 'summary' worksheet
    summary.append_row([new_month, total_income, total_outgoings, balance])
    

    if not month_rows:
        print(f"no data available for {new_month}.")
    else:
        print(f"Data for {new_month}:")
        for row in month_rows:
            print(row)
        print(f'Total Income: {total_income}, Total Outgoings :{total_outgoings}, Balance: {balance}')


def main():
    """
    Welcome Message to the user with options to chose from for the next step.
    """


    print('*** WELCOME TO BUDGET TRACKER ***\n')
    print('WOULD YOU LIKE TO GET CLEAR ON WHERE YOUR MONEY GOES ?\n')
    print("LET'S GET STARTED THEN!\n")


    # loop throught the choices2
    # Source : Python Exception Handling(CI)
    while True:
        print('Please choose from the following options: \n')
        print('1. Display Budget Summary\n')
        print('2. Generate Budget\n')
        print('3. Edit Budget\n')
        try:
            choice = int(input('Enter Your Choice ( 1, 2 or 3) Here:  '))
            print("\n")
            if choice == 1:
                budget_summary(new_month)
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



