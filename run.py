import gspread
from google.oauth2.service_account import Credentials
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ADHDSuperheros')

def main_menu():
    """
    Displays welcome message to user
    Provides user with menu options
    """
    print("Welcome to the ADHD Superhros app")
    time.sleep(3)
    print("1. Use app")
    print("2. Learn how to use app")
    print("3. Learn about ADHD")
    print("4. Exit")
    time.sleep(3)
    win_str = input("Enter your choice 1-4 below\n")
    # 1 = main()
    # 2 = learn_app() - to be defined
    # 3 = learn_adhd() - to be defined
    # 4 = exit() - to be defined

def get_strengths_data():
    """
    Get strengths from strengths worksheet least recently used.
    Print for user to be reminded.
    """
    strengths = SHEET.worksheet("strengths")
    strengths_row = strengths.get_all_values()
    print(strengths_row[-1])
    # Add code to update last presented data of strength
    # Decide which code is better for strength and advice functions


def get_advice_data():
    """
    Get advice from advice worksheet least recently used.
    Print to display to user.
    """
    advice = SHEET.worksheet("advice").get_all_values()
    advice_row = advice[-1]
    print(advice_row)
    # Add code to update last presented data of advice


def get_last_3_priorities():
    """
    Get previous days top 3 priorities.
    Present to user to confirm if done or not done on previous day.
    """
    dailytopthree = SHEET.worksheet("dailytopthree")

    columns = []
    for num in range(1, 3):
        column = dailytopthree.col_values(num)
        columns.append(column[-3:])

    print(columns)
    # Add code so user can input whether task was done or not.


def get_current_wins():
    """
    Get 3 wins from previous day from user
    """
    while True:
        print("Its important to take time to document your wins")
        time.sleep(3)
        print("Focusing your thoughts on past progress")
        print("leads to future progress")
        time.sleep(3)
        print("Your win will need to have a minimum of 10 words")
        time.sleep(3)
        print("Example: I cleared all my emails by lunchtime")
        print("and worked on my project in the afternoon as scheduled")
        time.sleep(3)
        win_str = input("Enter your win here:\n")
        win_data = win_str.split(",")
        # #Add code to ensure win_data saves as a string

        # if validate_data(win_data):
        # #     print("Example is not strong enough. Try more detail!")
        # #     break

        return win_data

# def validate_data(values):
#     """
#     Inside the try, raises ValueError if string less than 6 words
#     """
#     try:
#         if len(values) < 10:
#             raise ValueError(
#                 f"At least 10 words are required, you provided len(values)"
#             )
#         except ValueError as e:
#             print(f"Invalid data enetered: {e}, please try again.\n")
#             return False

#         return True.


def update_wins_worksheet(data):
    """
    Receives a string to be inserted into wins worksheet
    Update the wins worksheet with the data provided
    """
    print("Updating your wins worksheet...\n")
    worksheet_to_update = SHEET.worksheet("wins")
    print(data)
    worksheet_to_update.append_row(data)
    print("Your wins worksheet update successfully\n")


def main():
    """
    Run all program functions
    """
    get_strengths_data()
    get_advice_data()
    get_last_3_priorities()
    data = get_current_wins()
    update_wins_worksheet(data)


main()
