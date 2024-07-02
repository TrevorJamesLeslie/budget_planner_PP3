import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
    
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


##const for security, file not to be tracked 
CREDS = Credentials.from_service_account_file('creds.json')
#const for credentials scoped
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
#const to allow auth of gspread client within these scoped credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
#const to open spread sheet
SHEET = GSPREAD_CLIENT.open('budget_planner')

tracker = SHEET.worksheet('tracker')
data = tracker.get_all_values() 

print(data)

def main():
    """
    Welcome message is displayed to the user explaining the main concept of the tracker
    """

    print('*** WELCOME TO BUDGET TRACKER ***\n')
    print('Would you like to get clear on where your money goes?')
    print("Let's get started!")
    print('Please choose from the following options: ')
    print('\n')
    print('1. Display Budget Summary\n')
    print('2. Generate Budget\n')
    print('3. Edit Budget\n')

    #loop throught the choices
    #Python Exception Handling(CI)
    while True:
        try:
            choice = int(input('Please Enter Your Choice : \n'))
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
                print('Number Out Of Range. Please Enter Number From The List.\n')
        except ValueError:
            print('Invalid Data. Please Enter Number From The List.\n')
            continue
#calling the main function        
main()








