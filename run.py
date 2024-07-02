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

