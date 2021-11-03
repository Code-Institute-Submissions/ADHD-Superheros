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


def get_last_3_priorities():
    """
    Get previous days top 3 priorities.
    Present to user to confirm if done or not done on previous day.
    """
    dailytopthree = SHEET.worksheet("dailytopthree")

    columns = []
    for ind in range(1, 3):
        column = dailytopthree.col_values(ind)
        columns.append(column[-3:])

    print(columns)
    # Add code so user can input whether task was done or not.


def get_current_wins():
    """
    Get 3 wins from previous day from user
    """
    while True:
        print("Its importnat to take time to document your wins")
        print("Focusing your thoughts on past progress")
        print("leads to future progress")
        print("Your win will need to have a minimum of 10 words")
        print("Example: I cleared all my emails by luchtime")
        print("and worked on my project in the afteroon as scheduled")

        win_str = input("Enter your win here:\n")
        win_data = str(win_str)
        # win_data = win_str
        # #Add code to ensure win_data saves as a string

        # if validate_data(win_data):
        # #     print("Example is not strong enough. Try more detail!")
        # #     break
        print(win_data)

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
    worksheet_to_update.append_row(data)
    print("Your wins worksheet update successfully\n")


def main():
    """
    Run all program functions
    """
    get_strenghts_data()
    get_advice_data()
    get_last_3_priorities()
    get_current_wins()
    data = get_current_wins()
    update_wins_worksheet(data)


main()
