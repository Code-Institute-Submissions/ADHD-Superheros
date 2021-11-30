import time
# https://www.geeksforgeeks.org/python-datetime-module/
from datetime import date, timedelta, datetime
import os
import re
import gspread
from google.oauth2.service_account import Credentials
from random import randrange
from colorama import Fore, Back, Style  # https://pypi.org/project/colorama/
import pyfiglet
if os.path.exists("env.py"):
    import env  # noqa

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

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
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
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
        time.sleep(2.5)
        clear()
        main_menu()


def learn_app():
    """
    Privders user with instructions on how to use app
    """
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "How to use the app")
    print('\n')
    print(Fore.WHITE + "Below is a summary of each of the menu options")
    print('\n')
    time.sleep(1)
    # Option 1 
    print(Fore.WHITE + "1. Use app")
    print('\n')
    time.sleep(1)
    print(Fore.BLUE + "* Shares a daily reminder of a strength and advice related to ADHD.")
    time.sleep(1)
    print(Fore.CYAN + "* Review previous top 3 priorities and confirm if completed.")
    time.sleep(1)
    print(Fore.BLUE + "* Calculates your average completed priorities for the last 7 and 30 days.")
    time.sleep(1)
    print(Fore.CYAN + "* You'll be asked to provide a win/success for the previous day.")
    time.sleep(1)
    print(Fore.BLUE + "* You'll be asked for your email and a summary email will be sent to you.")
    print('\n')
    time.sleep(1)
    learn_page = input(Fore.WHITE +"Press enter to load next screen about using the app\n")
    print('\n')
    # Option 2 - add clear ()
    print(Fore.WHITE + "2. Learn how to use app")
    print('\n')
    time.sleep(1)
    print(Fore.BLUE + "* You'll be provided with an overview of each of the menu options.")
    time.sleep(1)
    print(Fore.CYAN + "* You'll get a sense of what to expect in particular for option 1 - Use app.")
    time.sleep(1)
    print('\n')
    learn_page = input(Fore.WHITE +"Press enter to load next screen about using the app\n")
    print('\n')
    # Option 3 - add clear ()
    print(Fore.WHITE + "3. Learn about ADHD")
    print('\n')
    time.sleep(1)
    print(Fore.BLUE + "* You'll be presented with education information about ADHD.")
    time.sleep(1)
    print(Fore.CYAN + "* The information is sourced from national and internationl experts.")
    time.sleep(1)
    print('\n')
    learn_page = input(Fore.WHITE +"Press enter to load next screen about using the app\n")
    print('\n')
    # Option 4 - add clear ()
    print(Fore.WHITE + "4. Exit")
    print('\n')
    time.sleep(1)
    print(Fore.BLUE + "* You'll be presented with two choice - return to main menu or the app will clear the screen.")
    time.sleep(1)
    print(Fore.CYAN + "* You can always return by reopening the app if you leave by mistake.")
    time.sleep(1)
    print('\n')
    print(Fore.WHITE + "Thank you for learning how to use the app. You'll now be presented with menu options.")
    print('\n')
    learn_page = input(Fore.WHITE +"Press enter to load your menu options\n")
    print('\n')
    print("1. Main menu")
    time.sleep(1)
    print("2. Exit")
    time.sleep(1)
    print('\n')
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
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Learn about ADHD - Part 1/2")
    print('\n')
    print(Fore.WHITE + "ADHD stands for attention deficit hyperactivity disorder.")
    time.sleep(1)
    print("It is a complex brain disorder that impacts 11% of children and almost 5% of adults.")
    time.sleep(1)
    print("ADHD is a developmental impairment of the brain’s executive functions.")
    print('\n')
    time.sleep(1)
    print(Fore.BLUE + "* ADHD is not a behaviour disorder.")
    time.sleep(1)
    print(Fore.CYAN + "* ADHD is not a mental illness. ")
    time.sleep(1)
    print(Fore.BLUE + "* ADHD is not a specific learning disability.")
    time.sleep(1)
    print('\n')
    print(Fore.WHITE + "ADHD is, instead, a developmental impairment of the brain’s self-management system.")
    print('\n')
    time.sleep(1)
    adhd_page = input(Fore.WHITE +"Press enter to load next screen about ADHD\n")
    print('\n')
    # clear() will decomment once testing is done
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Learn about ADHD - Part 2/2")
    print('\n')
    print(Fore.WHITE + "Adults with ADHD have problems in six major areas of executive functioning:")
    print('\n')
    time.sleep(1)
    print(Fore.BLUE + "* Activation – Problems with organization, prioritizing, and starting tasks.")
    time.sleep(1)
    print(Fore.CYAN + "* Focus – Problems with sustaining focus and resisting distraction, especially with reading.")
    time.sleep(1)
    print(Fore.BLUE + "* Effort – Problems with motivation, sustained effort, and persistence.")
    time.sleep(1)
    print(Fore.CYAN + "* Emotion – Difficulty regulating emotions and managing stress.")
    time.sleep(1)
    print(Fore.BLUE + "* Memory – Problems with short-term memory and memory retrieval.")
    time.sleep(1)
    print(Fore.CYAN + "* Action – Problems with self-control and self-regulation.")
    time.sleep(1)
    print('\n')
    print(Fore.WHITE +"Thank you for taking the time to learn about ADHD")
    print('\n')
    adhd_page = input("Press enter to load your exit options\n")
    # clear() will decomment once testing is done
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    time.sleep(1)
    print("1. Main menu")
    time.sleep(1)
    print("2. Exit")
    time.sleep(1)
    print('\n')
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
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "You're about to leave the app")
    print('\n')
    print("We hope you got value from the time spent using the app today.")
    print('\n')
    time.sleep(1)
    print("You'll now get a option to return to main menu or close the app.")
    print('\n')
    print("After the app is closed, you can reopen it to access the main menu.")
    print('\n')
    print("1. Main menu")
    print("2. Close app")
    time.sleep(2)
    leaving_choice = input("Enter your choice 1-2 below\n")
    if leaving_choice == '1':
        main_menu()
    elif leaving_choice == '2':
        clear()
    else:
        print("You must choose option 1 or 2")
        time.sleep(2)


def get_strengths_data():
    """
    Get strengths from strengths worksheet least recently used.
    Print for user to be reminded.
    """
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    global STRENGTH_NAME
    global STRENGTH_DETAIL
    strengths = SHEET.worksheet("strengths")
    row_count = len(strengths.col_values(1))
    row_ref_start = row_count + 2
    random_row = strengths.row_values(randrange(1, row_ref_start))
    time.sleep(2)
    print(random_row[0])
    print(random_row[1])
    STRENGTH_NAME = random_row[0]
    STRENGTH_DETAIL = random_row[1]
    print('ADHD is like having superpowers if you focus on your strengths enough.')
    print(f'Today, try to think about examples where the strength of {STRENGTH_NAME}. {STRENGTH_DETAIL}')
    # Decide which code is better for strength and advice functions


def get_advice_data():
    """
    Get advice from advice worksheet least recently used.
    Print to display to user.
    """
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    global ADVICE_NAME
    global ADVICE_DETAIL
    advice = SHEET.worksheet("advice")
    row_count = len(advice.col_values(1))
    row_ref_start = row_count + 2
    random_row = advice.row_values(randrange(1, row_ref_start))
    time.sleep(2)
    ADVICE_NAME = random_row[0]
    ADVICE_DETAIL = random_row[1]
    print('Great advice is worth repeating.')
    print(f'Today, give some thought to the advice {ADVICE_NAME}. {ADVICE_DETAIL}')
    # Add code to update last presented data of advice


def get_last_3_priorities():
    """
    Get previous days top 3 priorities.
    Present to user to confirm if done or not done on previous day.
    """
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
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
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    dailytopthree = SHEET.worksheet("dailytopthree")
    wk_start_date = date.today() - timedelta(days=7)
    wk_end_date = date.today()
    print(wk_start_date)
    print(wk_end_date)

    wktotal = 0  # total priorities in last 7 days
    wkdone = 0  # priorities with status done in last 7 days

    rows = dailytopthree.get_all_values()
    for i, row in enumerate(rows):
        if i > 0:
            dt_w = datetime.strptime(row[0], "%d/%m/%Y").date()
            if dt_w >= wk_start_date and dt_w <= wk_end_date:
                if row[3] == 'done':
                    wkdone += 1
                wktotal += 1
    print(wkdone)
    print(wktotal)
    if wktotal == 0:
        print("There are no priorites for the last 7 days")
        print("If you log priorties more often, we'll have data to share")
    else:
        weekly_avg_num = (wkdone / wktotal)
        weekly_avg_per = "{:.0%}".format(weekly_avg_num)
        print(f'Your average % of completed priorities for the last 7 days is {weekly_avg_per}')


def calc_month_avg():
    """
    Get last 30 days of total priorities (complete & incomplete)
    Calculate %  done of total priorities
    """
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    dailytopthree = SHEET.worksheet("dailytopthree")
    mth_start_date = date.today() - timedelta(days=30)
    mth_end_date = date.today()
    print(mth_start_date)
    print(mth_end_date)

    mthtotal = 0  # total priorities in last 30 days
    mthdone = 0  # priorities with status done in last 30 days

    rows = dailytopthree.get_all_values()
    for i, row in enumerate(rows):
        if i > 0:
            dt_m = datetime.strptime(row[0], "%d/%m/%Y").date()
            if dt_m >= mth_start_date and dt_m <= mth_end_date:
                if row[3] == 'done':
                    mthdone += 1
                mthtotal += 1
    print(mthdone)
    print(mthtotal)
    if mthtotal == 0:
        print("There are no priorites for the last 30 days")
        print("If you log priorties more often, we'll have data to share")
    else:
        month_avg_num = (mthdone / mthtotal)
        month_avg_per = "{:.0%}".format(month_avg_num)
        print(f'Your average % of completed priorities for the last 30 days is {month_avg_per}')


def get_current_wins():
    """
    Get 3 wins from previous day from user
    """
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
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


def get_email():
    global USER_EMAIL
    while True:
        USER_EMAIL = input("Please enter your email: \n")
        regex = r"^[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]{3,252}\.[a-zA-Z]{2,}$"

        if not re.fullmatch(regex, USER_EMAIL):
            clear()
            print(f"'{USER_EMAIL}' is Invalid, enter a real email address!\n")
        else:
            clear()
            print("Thank you for entering your email!\n")
            break
    return USER_EMAIL


def email_send():
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = USER_EMAIL
    msg["Subject"] = "Your ADHD Superhero Summary!"
    format_email = (
        f"Thank you for taking the time today to use the ADHD Superheros App.\n"

        f"This emails purpose is summarise what we have covered today.\n"

        f"It's important to focus on your strenghts. Today's strength is {STRENGTH_NAME}\n"

        f"{STRENGTH_DETAIL}\n"

        f"Great advice is worth repeating. Today's advice focused on {ADVICE_NAME}\n"
      
        f"{ADVICE_DETAIL}\n"

        f"Great advice is worth repeating. Today's advice focused on {ADVICE_NAME}\n"
    )
    msg.attach (MIMEText(str(format_email), "html"))
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(EMAIL, PASSWORD)
    smtpserver.send_message(msg)
    smtpserver.quit()


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
    get_email()
    email_send()


main_menu()
