from datetime import datetime

user_name = input('\nWhat\'s your name? ')
user_birth_month = input('\nGreat! What month were you born? ')
# Get current month, spelled out
current_month = datetime.now().strftime("%B") # Taken from https://www.itsolutionstuff.com/post/how-to-get-current-month-in-pythonexample.html#:~:text=main.py-,from%20datetime%20import%20datetime%20today%20%3D%20datetime.,%2C%20month1)%3B%20month2%20%3D%20today.

print(f'\nHello, {user_name}!')

num_letters_in_name = len(user_name)

print(f'\nYou have {num_letters_in_name} letters in your name.')

if user_birth_month == current_month:
    print('Happy birthday month!')

