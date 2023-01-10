from datetime import datetime

def main():

    user_name, user_birth_month = get_user_input() # Get return values from function

    print(f'\nHello, {user_name}!')
    num_letters_in_name = len(user_name)
    print(f'\nYou have {num_letters_in_name} letters in your name.')

    current_month = get_current_month() # Get current month from function
    is_birthday_month = compare_months(user_birth_month, current_month) # Call function to compare current month with input from user

    if is_birthday_month: # If current month and user birthday month are the same, print message
        print('\nHappy birthday month!')

def get_current_month():
    # Get current month, spelled out
    current_month = datetime.now().strftime("%B") # Taken from https://www.itsolutionstuff.com/post/how-to-get-current-month-in-pythonexample.html#:~:text=main.py-,from%20datetime%20import%20datetime%20today%20%3D%20datetime.,%2C%20month1)%3B%20month2%20%3D%20today.
    return current_month

def get_user_input(): # Ask user for name and birthday month
    user_name = input('\nWhat\'s your name? ')
    user_birth_month = input('\nGreat! What month were you born? ')
    return user_name, user_birth_month

def compare_months(user_birth_month, current_month): # Compare user birthday month to current month, case-insensitively
    if user_birth_month.lower() == current_month.lower():
        return True
    else:
        return False

main()