import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ADHDSuperheros')


def get_strenghts_data():
    """
    Get strenghts from strenghts worksheet least recently used.
    Print for user to be reminded.
    """
    strenghts = SHEET.worksheet("strenghts")
    strenghts_row = strenghts.get_all_values()
    print(strenghts_row[-1])
    # Add code to update last presented data of strenght
    # Decide which code is better for strenght and advice functions


def get_advice_data():
    """
    Get advice from advice worksheet least recently used.
    Print to display to user. 
    """
    advice = SHEET.worksheet("advice").get_all_values()
    advice_row = advice[-1]
    print(advice_row)
    # Add code to update last presented data of advice


# def get_last_3_priorities():
#     """
#     Get previous days top 3 priorities.
#     Present to user to confirm if done or not done on previous day.
#     """


def main():
    """
    Run all program functions
    """
    get_strenghts_data()
    get_advice_data()

main()