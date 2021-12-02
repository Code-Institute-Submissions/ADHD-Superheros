import time
# https://www.geeksforgeeks.org/python-datetime-module/
from datetime import date, timedelta, datetime
import os
import re
import gspread
import pyfiglet
from google.oauth2.service_account import Credentials
from random import randrange
from colorama import Fore, Style, init  # https://pypi.org/project/colorama/
init(autoreset=True)
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
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Welcome to the ADHD Superheros app")
    print('\n')
    time.sleep(0.5)
    print(Fore.BLUE + "1. Use app")
    time.sleep(0.5)
    print(Fore.BLUE + "2. Learn how to use app")
    time.sleep(0.5)
    print(Fore.BLUE + "3. Learn about ADHD")
    time.sleep(0.5)
    print(Fore.BLUE + "4. Exit")
    print('\n')
    time.sleep(1)
    menu_choice = input("Enter your choice 1-4 below\n")
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
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "How to use the app")
    print('\n')
    print(Fore.WHITE + "Below is a summary of each of the menu options.")
    print('\n')
    time.sleep(1)
    # Option 1
    print(Fore.WHITE + "1. Use app")
    print('\n')
    time.sleep(1)
    print(
        Fore.BLUE + "* Shares a daily reminder of "
        "a strength and advice related to ADHD.")
    time.sleep(1)
    print(
        Fore.CYAN + "* Review previous top 3 "
        "priorities and confirm if completed.")
    time.sleep(1)
    print(
        Fore.BLUE + "* Calculates your average completed "
        "priorities for the last 7 and 30 days.")
    time.sleep(1)
    print(
        Fore.CYAN + "* You'll be asked to provide "
        "a win/success for the previous day.")
    time.sleep(1)
    print(
        Fore.BLUE + "* You'll be asked for your email "
        "and a summary email will be sent to you.")
    print('\n')
    time.sleep(1)
    input(
        Fore.WHITE + "Press enter to load the next "
        "screen about using the app")
    print('\n')
    # Option 2
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.WHITE + "2. Learn how to use app")
    print('\n')
    time.sleep(1)
    print(
        Fore.BLUE + "* You'll be provided with an overview "
        "of each of the menu options.")
    time.sleep(1)
    print(
        Fore.CYAN + "* You'll get a sense of what to expect "
        "in particular for option 1 - Use app.")
    time.sleep(1)
    print('\n')
    input(
        Fore.WHITE + "Press enter to load the next "
        "screen about using the app")
    print('\n')
    # Option 3
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.WHITE + "3. Learn about ADHD")
    print('\n')
    time.sleep(1)
    print(
        Fore.BLUE + "* You'll be presented with education "
        "information about ADHD.")
    time.sleep(1)
    print(
        Fore.CYAN + "* The information is sourced from "
        "national and internationl experts.")
    time.sleep(1)
    print('\n')
    input(
        Fore.WHITE + "Press enter to load the next "
        "screen about using the app\n")
    print('\n')
    # Option 4
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.WHITE + "4. Exit")
    print('\n')
    time.sleep(1)
    print(
        Fore.BLUE + "* You'll be presented with two choices "
        "- return to main menu or the app will clear the screen.")
    time.sleep(1)
    print(
        Fore.CYAN + "* You can always return by reopening "
        "the app if you leave by mistake.")
    time.sleep(1)
    print('\n')
    print(
        Fore.WHITE + "Thank you for learning how to use the app. "
        "You'll now be presented with menu options.")
    print('\n')
    input(Fore.WHITE + "Press enter to load your menu options\n")
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print("Your menu options")
    print('\n')
    time.sleep(1)
    print("1. Main menu")
    time.sleep(1)
    print("2. Exit")
    time.sleep(1)
    print('\n')
    while True:
        learn_choice = input("Enter your choice 1-2 below\n").strip()
        if learn_choice == "1":
            main_menu()
            break
        elif learn_choice == "2":
            leaving()
            break
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
    # Part 1 of 2
    print(Fore.RED + "Learn about ADHD - Part 1/2")
    print('\n')
    print(
        Fore.WHITE + "ADHD stands for attention deficit "
        "hyperactivity disorder.")
    time.sleep(1)
    print(
        "It is a complex brain disorder that impacts "
        "11% of children and almost 5% of adults.")
    time.sleep(1)
    print(
        "ADHD is a developmental impairment of "
        "the brain’s executive functions.")
    print('\n')
    time.sleep(1)
    print(Fore.BLUE + "* ADHD is not a behaviour disorder.")
    time.sleep(1)
    print(Fore.CYAN + "* ADHD is not a mental illness. ")
    time.sleep(1)
    print(Fore.BLUE + "* ADHD is not a specific learning disability.")
    time.sleep(1)
    print('\n')
    print(
        Fore.WHITE + "ADHD is, instead, a developmental "
        "impairment of the brain’s self-management system.")
    print('\n')
    time.sleep(1)
    input(Fore.WHITE + "Press enter to load next screen about ADHD\n")
    print('\n')
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    # Part 2 of 2
    print(Fore.RED + "Learn about ADHD - Part 2/2")
    print('\n')
    print(
        Fore.WHITE + "Adults with ADHD have problems in "
        "six major areas of executive functioning:")
    print('\n')
    time.sleep(1)
    print(
        Fore.BLUE + "* Activation – Problems with "
        "organization, prioritizing, and starting tasks.")
    time.sleep(1)
    print(
        Fore.CYAN + "* Focus – Problems with sustaining "
        "focus and resisting distraction, especially with reading.")
    time.sleep(1)
    print(
        Fore.BLUE + "* Effort – Problems with motivation, "
        "sustained effort, and persistence.")
    time.sleep(1)
    print(
        Fore.CYAN + "* Emotion – Difficulty regulating "
        "emotions and managing stress.")
    time.sleep(1)
    print(
        Fore.BLUE + "* Memory – Problems with short-term "
        "memory and memory retrieval.")
    time.sleep(1)
    print(
        Fore.CYAN + "* Action – Problems with self-control "
        "and self-regulation.")
    time.sleep(1)
    print('\n')
    print(Fore.WHITE + "Thank you for taking the time to learn about ADHD")
    print('\n')
    input(Fore.WHITE + "Press enter to load your menu options\n")
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print("Your menu options")
    print('\n')
    time.sleep(1)
    print("1. Main menu")
    time.sleep(1)
    print("2. Exit")
    time.sleep(1)
    print('\n')
    while True:
        learn_choice = input("Enter your choice 1-2 below\n").strip()
        if learn_choice == "1":
            main_menu()
        elif learn_choice == "2":
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
    print(
        "After the app is closed, you can "
        "reopen it to access the main menu.")
    print('\n')
    print("1. Main menu")
    print("2. Close app")
    time.sleep(2)
    while True:
        leaving_choice = input("Enter your choice 1-2 below\n").strip()
        if leaving_choice == "1":
            main_menu()
        elif leaving_choice == "2":
            clear()
            print("Thanks for visiting ADHD Superheros!")
        else:
            print("You must choose option 1 or 2")
            time.sleep(2)


def get_strengths_data():
    """
    Get random strength from strengths worksheet.
    """
    global STRENGTH_NAME
    global STRENGTH_DETAIL
    clear()
    print("Your strenghts data is loading.....")
    strengths = SHEET.worksheet("strengths")
    row_count = len(strengths.col_values(1))
    row_ref_start = row_count + 2
    random_row = strengths.row_values(randrange(2, row_ref_start))
    STRENGTH_NAME = random_row[0]
    STRENGTH_DETAIL = random_row[1]
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    time.sleep(1)
    print(Fore.RED + "ADHD Strenghts")
    print('\n')
    time.sleep(1)
    print(
        Fore.WHITE + "ADHD is like having superpowers "
        "if you focus on your strengths enough.")
    print('\n')
    time.sleep(1)
    print(
        Fore.BLUE + "Today, try to think about examples "
        f"where you've used the strength of {STRENGTH_NAME}.")
    print('\n')
    time.sleep(1)
    print(Fore.CYAN + f'{STRENGTH_DETAIL}.')
    print('\n')
    time.sleep(1)
    input(Fore.WHITE + "Press enter to load your daily advive reminder\n")
    print('\n')


def get_advice_data():
    """
    Get advice from advice worksheet least recently used.
    Print to display to user.
    """
    global ADVICE_NAME
    global ADVICE_DETAIL
    clear()
    print("Your advice data is loading.....")
    advice = SHEET.worksheet("advice")
    row_count = len(advice.col_values(1))
    row_ref_start = row_count + 2
    random_row = advice.row_values(randrange(2, row_ref_start))
    ADVICE_NAME = random_row[0]
    ADVICE_DETAIL = random_row[1]
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "ADHD Advice \n")
    time.sleep(1)
    print(Fore.WHITE + 'Great advice is worth repeating.\n')
    time.sleep(1)
    print(
        Fore.BLUE + "Today, give some thought "
        f"to the advice on {ADVICE_NAME}.'\n")
    time.sleep(1)
    print(Fore.CYAN + f'{ADVICE_DETAIL}.\n')
    time.sleep(1)
    input(
        Fore.WHITE + "Press enter to review your "
        "previous top 3 priorities.\n")
    time.sleep(1)


def get_last_3_priorities():
    """
    Get previous days top 3 priorities.
    Present to user to confirm if done or not done on previous day.
    """
    global OLDPRIORITY1
    global OLDPRIORITY2
    global OLDPRIORITY3
    global TASKSTATUS1
    global TASKSTATUS2
    global TASKSTATUS3
    dailytopthree = SHEET.worksheet("dailytopthree")
    max_rows = len(dailytopthree.get_all_values())
    columns = []
    for num in range(1, 5):
        column = dailytopthree.col_values(num)
        columns.append(column[-3:])
    OLDPRIORITY1 = (columns[2][0])
    OLDPRIORITY2 = (columns[2][1])
    OLDPRIORITY3 = (columns[2][2])
    # Priority 1
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Review previous top 3 priorities \n")
    time.sleep(1)
    print(
        Fore.WHITE + "The first priority to review is "
        f"{OLDPRIORITY1} from {columns[0][0]}.\n")
    time.sleep(1)
    while True:
        TASKSTATUS1 = input(
            Fore.BLUE + "Please confirm if this "
            "priority was done or undone.\n")
        if TASKSTATUS1 == "done":
            break
        if TASKSTATUS1 == "undone":
            break
        else:
            print(Fore.WHITE + "Only done or undone will be accepted.\n")
            time.sleep(2)
    print('\n')
    print(
        Fore.CYAN + f"Thank you for confirming status of {OLDPRIORITY1} "
        f"is {TASKSTATUS1}.\n")
    time.sleep(1)
    print(Fore.GREEN + "We are updating your priorities worksheet...\n")
    time.sleep(1)
    dailytopthree.update_cell((max_rows - 2), 4, str(TASKSTATUS1))
    print(Fore.GREEN + "Your priorities worksheet update successfully\n")
    time.sleep(1)
    input(Fore.WHITE + "Press enter to review next priority\n")
    print('\n')
    # Priority 2
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Review previous top 3 priorities \n")
    time.sleep(1)
    print(
        Fore.WHITE + f"The second priority to review is {OLDPRIORITY2} "
        f"from {columns[0][1]}.\n")
    time.sleep(1)
    while True:
        TASKSTATUS2 = input(
            Fore.BLUE + "Please confirm if this priority "
            "was done or undone.\n")
        if TASKSTATUS2 == "done":
            break
        if TASKSTATUS2 == "undone":
            break
        else:
            print(Fore.WHITE + "Only done or undone will be accepted.\n")
            time.sleep(2)
    print('\n')
    print(
        Fore.CYAN + f"Thank you for confirming status of {OLDPRIORITY2} "
        f"is {TASKSTATUS2}.\n")
    time.sleep(1)
    print(Fore.GREEN + "We are updating your priorities worksheet...\n")
    time.sleep(1)
    dailytopthree.update_cell((max_rows - 1), 4, str(TASKSTATUS2))
    print(Fore.GREEN + "Your priorities worksheet update successfully\n")
    time.sleep(1)
    input(Fore.WHITE + "Press enter to review next priority\n")
    print('\n')
    # Priority 3
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Review previous top 3 priorities \n")
    time.sleep(1)
    print(
        Fore.WHITE + f"The third priority to review is {OLDPRIORITY3} "
        f"from {columns[0][2]}.\n")
    time.sleep(1)
    while True:
        TASKSTATUS3 = input(
            Fore.BLUE + "Please confirm if this "
            "priority was done or undone.\n")
        if TASKSTATUS3 == "done":
            break
        if TASKSTATUS3 == "undone":
            break
        else:
            print(Fore.WHITE + "Only done or undone will be accepted.\n")
            time.sleep(2)
    print('\n')
    print(
        Fore.CYAN + f"Thank you for confirming status of {OLDPRIORITY3} "
        f"is {TASKSTATUS3}.\n")
    time.sleep(1)
    print(Fore.GREEN + "We are updating your priorities worksheet...\n")
    time.sleep(1)
    dailytopthree.update_cell((max_rows), 4, str(TASKSTATUS3))
    print(Fore.GREEN + "Your priorities worksheet update successfully\n")
    time.sleep(1)
    print(Fore.WHITE + "You finished reviewing your priorities.\n")
    input(
        Fore.WHITE + "Press enter to view your "
        "weekly and monthly reports.\n")
    print('\n')

def get_today_priorities():
    """
    Get todays top 3 priorities.
    """
    global NEWPRIORITY1
    global NEWPRIORITY2
    global NEWPRIORITY3
    dailytopthree = SHEET.worksheet("dailytopthree")
    max_rows = len(dailytopthree.get_all_values())
    taskdate = date.today()
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Enter today's top 3 priorities.\n")
    time.sleep(1)
    print(
        "Today's priorities can be new ones, or "
        "they can be undone ones from the previous day.\n")
    time.sleep(1)
    print(
        "Don't forget that priorties can be to "
        "go do something fun or relaxing. Time off is important!\n")
    time.sleep(1)
    # Priority 1
    NEWPRIORITY1 = input(
        Fore.BLUE + "What will be your first priority for today?\n")
    dailytopthree.update_cell((max_rows + 1), 1, str(taskdate))
    dailytopthree.update_cell((max_rows + 1), 3, str(NEWPRIORITY1))
    time.sleep(1)
    print('\n')
    # Priority 2
    NEWPRIORITY2 = input(
        Fore.CYAN + "What will be your second priority for today?\n")
    dailytopthree.update_cell((max_rows + 2), 1, str(taskdate))
    dailytopthree.update_cell((max_rows + 2), 3, str(NEWPRIORITY2))
    time.sleep(1)
    print('\n')
    # Priority 3
    NEWPRIORITY3 = input(
        Fore.BLUE + "What will be your third priority for today?\n")
    dailytopthree.update_cell((max_rows + 3), 1, str(taskdate))
    dailytopthree.update_cell((max_rows + 3), 3, str(NEWPRIORITY3))
    time.sleep(1)
    print('\n')
    # Summary
    print("Thank you for providing your top 3 priorities for today.\n")
    time.sleep(1)
    print(
        Fore.GREEN + f"Your top 3 priorities for today are {NEWPRIORITY1}"
        f", {NEWPRIORITY2} and {NEWPRIORITY3}.\n")
    time.sleep(1)


def calc_weekly_avg():
    """
    Get last 7 days of total priorities (complete & incomplete)
    Calculate %  done of total priorities
    """
    global WKTOTAL
    global WKDONE
    global WEEKLY_AVG_PERC
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Your weekly report.")
    print('\n')
    dailytopthree = SHEET.worksheet("dailytopthree")
    wk_start_date = date.today() - timedelta(days=7)
    wk_end_date = date.today()
    WKTOTAL = 0  # total priorities in last 7 days
    WKDONE = 0  # priorities with status done in last 7 days
    rows = dailytopthree.get_all_values()
    for i, row in enumerate(rows):
        if i > 0:
            dt_w = datetime.strptime(row[0], "%d/%m/%Y").date()
            if dt_w >= wk_start_date and dt_w <= wk_end_date:
                if row[3] == 'done':
                    WKDONE += 1
                WKTOTAL += 1
    if WKTOTAL == 0:
        print(Fore.BLUE + "There are no priorites for the last 7 days")
        print('\n')
        time.sleep(1)
        print(
            Fore.CYAN + "If you log priorties more often, "
            "we'll have data to share")
        print('\n')
        time.sleep(1)
        input(Fore.WHITE + "Press enter to view your monthly report.\n")
        print('\n')
    else:
        WEEKLY_AVG_PERC = "{:.0%}".format(WKDONE / WKTOTAL)
        print(
            Fore.BLUE + f"You entered {WKTOTAL} priorities "
            f"between {wk_start_date} and {wk_end_date}.")
        print('\n')
        time.sleep(1)
        print(Fore.CYAN + f'You completed {WKDONE} of {WKTOTAL} priorities.')
        print('\n')
        time.sleep(1)
        print(
            Fore.BLUE + f"Your average % of completed priorities"
            f"for the last 7 days is {WEEKLY_AVG_PERC}")
        print('\n')
        time.sleep(1)
        input(Fore.WHITE + "Press enter to view your monthly report.")
        print('\n')


def calc_month_avg():
    """
    Get last 30 days of total priorities (complete & incomplete)
    Calculate %  done of total priorities
    """
    global MTHTOTAL
    global MTHDONE
    global MONTH_AVG_PER
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Your monthly report.")
    print('\n')
    dailytopthree = SHEET.worksheet("dailytopthree")
    mth_start_date = date.today() - timedelta(days=30)
    mth_end_date = date.today()
    MTHTOTAL = 0  # total priorities in last 30 days
    MTHDONE = 0  # priorities with status done in last 30 days
    rows = dailytopthree.get_all_values()
    for i, row in enumerate(rows):
        if i > 0:
            dt_m = datetime.strptime(row[0], "%d/%m/%Y").date()
            if dt_m >= mth_start_date and dt_m <= mth_end_date:
                if row[3] == 'done':
                    MTHDONE += 1
                MTHTOTAL += 1
    if MTHTOTAL == 0:
        print(Fore.BLUE + "There are no priorites for the last 30 days")
        print('\n')
        time.sleep(1)
        print(
            Fore.CYAN + "If you log priorties more often, "
            "we'll have data to share")
        print('\n')
        time.sleep(1)
        input(Fore.WHITE + "Press enter to view your monthly report.\n")
        print('\n')
    else:
        MONTH_AVG_PER = "{:.0%}".format(MTHDONE / MTHTOTAL)
        print(
            Fore.BLUE + f"You entered {MTHTOTAL} priorities "
            f"between {mth_start_date} and {mth_end_date}.")
        print('\n')
        time.sleep(1)
        print(Fore.CYAN + f'You completed {MTHDONE} of {MTHTOTAL} priorities.')
        print('\n')
        time.sleep(1)
        print(
            Fore.BLUE + f"Your average % of completed priorities "
            f"for the last 30 days is {MONTH_AVG_PER}")
        print('\n')
        time.sleep(1)
        input(Fore.WHITE + "Press enter to submit your win or success.")
        print('\n')

def show_previous_wins():
    """
    Present user with 5 random previous wins
    """
    global OLDWIN1
    global OLDWIN2
    global OLDWIN3
    global OLDWIN4
    global OLDWIN5
    wins = SHEET.worksheet("wins")
    row_count = len(wins.col_values(1))
    row_ref_start = row_count + 1
    OLDWIN1 = (wins.row_values(randrange(2, row_ref_start))[0])
    OLDWIN2 = (wins.row_values(randrange(2, row_ref_start))[0])
    OLDWIN3 = (wins.row_values(randrange(2, row_ref_start))[0])
    OLDWIN4 = (wins.row_values(randrange(2, row_ref_start))[0])
    OLDWIN5 = (wins.row_values(randrange(2, row_ref_start))[0])
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Reminders of previous wins and successes\n")
    random1 = wins.row_values(randrange(2, row_ref_start))
    # win 1-5
    print(f'Your first win is {(OLDWIN1)}\n')
    print(f'Your second win is {OLDWIN2}\n')
    print(f'Your third win is {OLDWIN3}\n')
    print(f'Your fourth win is {OLDWIN4}\n')
    print(f'Your fift win is {OLDWIN5}\n')


def get_current_win():
    """
    Get a win/success from previous day from user
    """
    global WIN_DATA
    wins = SHEET.worksheet("wins")
    clear()
    ascii_banner = pyfiglet.figlet_format("ADHD Superheros")
    print(ascii_banner)
    print(Fore.RED + "Time to focus on a win or success\n")

    print(Fore.BLUE + "* Its important to take time to document your wins")
    time.sleep(1)
    print(
        Fore.CYAN + "* Focusing your thoughts on past "
        "progress and success leads to future progress\n")
    time.sleep(1)
    print(Fore.WHITE + "Your win will need to have a minimum of 10 words.\n")
    time.sleep(1)
    print(
        "Example: I cleared all my emails by lunchtime and "
        "worked on my project in the afternoon as scheduled\n")
    time.sleep(1)
    WIN_DATA = input("Enter your win here:\n")
    print(len(WIN_DATA))
    try:
        if len(WIN_DATA) < 6:
            raise ValueError(
                f"A minimum of 6 words required, you provided {len(WIN_DATA)}"
            )
        else:
            wins.append_row(str(WIN_DATA))
            print(Fore.GREEN + "Updating your wins worksheet...\n")
            time.sleep(1)
            print(Fore.GREEN + "Your wins worksheet update successfully\n")


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
    format_email = ("""<html>
            <body>
                <div>
                    <img src="https://raw.githubusercontent.com/declanosullivan/ADHD-Superheros/main/assets/images/emailheaderlogo.png" style="width: 100%; height: auto;">
                    <div style="text-align: left;">
                        <h2>Overview</h2>
                        <p>Thank you for taking the time today to use the ADHD Superheros App.</p>
                        <p>This emails purpose is summarise what we have covered today.</p>
                        <br>
                    </div>
                    <div style="text-align: left;">    
                        <h2>1. Today's strength</h2>
                        f"<p>It's important to focus on your strenghts. Today's strength is <strong>{STRENGTH_NAME}</strong>.</p>"
                        f"<p>{STRENGTH_DETAIL}</p>"
                        <br>
                    </div>
                    <div style="text-align: left;">    
                        <h2>'2. Today's advice'</h2>
                        <br>
                        <p> Great advice is worth repeating. Today's advice focused on $ADVICE_NAME </strong>."</p>
                        <br>
                        <p>f"{ADVICE_DETAIL}"</p>
                        <br>
                    </div>  
                        <h2>3. Your weekly and monthly report</h2>
                        <br>
                        <h2>4. Your previous top 3 priorities</h2>
                        <br>
                        <h2>1. Today's top 3 priorities</h2>
                    </div>
                </div>
            </body>
    </html>"""
    )
    msg.attach(MIMEText(str(format_email), "html"))
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
    # get_strengths_data()
    # get_advice_data()
    # get_last_3_priorities()
    # get_today_priorities()
    # calc_weekly_avg()
    # calc_month_avg()
    # show_previous_wins()
    # data = get_current_wins()
    # update_wins_worksheet(data)
    get_email()
    email_send()


main_menu()
