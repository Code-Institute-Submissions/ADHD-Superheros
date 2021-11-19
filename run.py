import time
# https://www.geeksforgeeks.org/python-datetime-module/
from datetime import date, timedelta, datetime
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back, Style  # https://pypi.org/project/colorama/
import os
import pyfiglet

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ADHDSuperheros')


def clear():
    """
    Clear the console/screen
    https://stackoverflow.com/questions/2084508/clear-terminal-in-python
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    """
    Displays welcome message to user
    Provides user with menu options
    """
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros!!")
    print(ascii_banner)
    print(Fore.RED + "Welcome to the ADHD Superheros app")
    print('\n')
    time.sleep(1)
    print(Fore.BLUE + "1. Use app")
    time.sleep(1)
    print("2. Learn how to use app")
    time.sleep(1)
    print("3. Learn about ADHD")
    time.sleep(1)
    print("4. Exit")
    print('\n')
    time.sleep(1)
    menu_choice = input(Style.RESET_ALL + "Enter your choice 1-4 below\n")
    time.sleep(1)
    if menu_choice == '1':
        main()
    elif menu_choice == '2':
        learn_app()
    elif menu_choice == '3':
        learn_adhd()
    elif menu_choice == '4':
        leaving()
    else:
        print("You must choose option 1, 2, 3 or 4")
        time.sleep(1)
        clear()
        main_menu()


def learn_app():
    """
    Privders user with instructions on how to use app
    """
    print("Optimise Daily Life while reducing cognitive overload")
    time.sleep(2)
    print("Now that you know how to use the app,")
    print("would you like to return to the main menu or exit?")
    print("1. Main menu")
    time.sleep(1)
    print("2. Exit")
    time.sleep(1)
    learn_choice = input("Enter your choice 1-2 below\n")
    if learn_choice == '1':
        main_menu()
    elif learn_choice == '2':
        leaving()
    else:
        print("You must choose option 1 or 2")
        time.sleep(2)


def learn_adhd():
    """
    Provides user with education info on ADHD
    """
    print("ADHD is neurotypical developmental disorder")
    print("charaterised by an impairment of executive function")
    time.sleep(2)
    print("Now that you know more about ADHD,")
    print("would you like to return to the main menu or exit?")
    print("1. Main menu")
    print("2. Exit")
    time.sleep(2)
    adhd_choice = input("Enter your choice 1-2 below\n")
    if adhd_choice == '1':
        main_menu()
    elif adhd_choice == '2':
        leaving()
    else:
        print("You must choose option 1 or 2")
        time.sleep(2)


def leaving():
    """
    Guides user out of app
    """
    print("We hope that even though you are leaving the app,")
    print("that you got value from your time spent here")
    print("If you leave this screen open,")
    print("you can return the main menu at anytime")
    print("You can also close and open the app again to access the main menu")
    print("1. Main menu")
    print("2. Close app")
    time.sleep(2)
    leaving_choice = input("Enter your choice 1-2 below\n")
    if leaving_choice == '1':
        main_menu()
    elif leaving_choice == '2':
        leaving()
    else:
        print("You must choose option 1 or 2")
        time.sleep(2)


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


def calc_weekly_avg():
    """
    Get last 7 days of total priorities (complete & incomplete)
    Calculate %  done of total priorities
    """
    dailytopthree = SHEET.worksheet("dailytopthree")
    wk_start_date = date.today() - timedelta(days=7)
    wk_end_date = date.today()
    print(wk_start_date)
    print(wk_end_date)
 
    wktotal = 0  # total prioritise in last 7 days
    wkdone = 0  # priorities with status done in last 7 days
    
    rows = dailytopthree.get_all_values()
    for i, row in enumerate(rows):
        if i > 0 :
            dt = datetime.strptime(row[0], "%d/%m/%Y").date()
            if dt >= wk_start_date and dt <= wk_end_date:
                if row[3] == 'done':
                    wkdone += 1
                wktotal += 1
    print(wkdone)
    print(wktotal)
    weekly_avg_num = (wkdone / wktotal)
    weekly_avg_per = "{:.0%}".format(weekly_avg_num)
    print(f'Your average % of completed priorities for the last 7 days is {weekly_avg_per}')


def calc_month_avg():
    """
    Get last 30 days of total priorities (complete & incomplete)
    Calculate %  done of total priorities
    """
    dailytopthree = SHEET.worksheet("dailytopthree")
    mth_start_date = date.today() - timedelta(days=30)
    mth_end_date = date.today()
    print(mth_start_date)
    print(mth_end_date)

    
    mthtotal = 0  # total prioritise in last 30 days
    mthdone = 0  # priorities with status done in last 30 days

    rows = dailytopthree.get_all_values()
    for i, row in enumerate(rows):
        if i > 0 :
            dtm = datetime.strptime(row[0], "%d/%m/%Y").date()
            if dtm >= mth_start_date and dtm <= mth_end_date:
                if row[3] == 'done':
                    mthdone += 1
                mthtotal += 1
    print(mthdone)
    print(mthtotal)
    month_avg_num = (mthdone / mthtotal)
    month_avg_per = "{:.0%}".format(month_avg_num)
    print(f'Your average % of completed priorities for the last 30 days is {month_avg_per}')


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
    calc_weekly_avg()
    calc_month_avg()
    data = get_current_wins()
    update_wins_worksheet(data)


main_menu()
