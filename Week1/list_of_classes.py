"""This program asks a user to add classes they are taking this semester to a list.
    It will then print out the classes they have written."""

print('\nCreate a list of classes you\'re taking this semester!')

user_classes = [] # List of classes

user_class = input('\nEnter a class, or press enter if you are done: ')

while user_class: # Loop until user presses enter (rendering user_class False)
    user_classes.append(user_class)
    user_class = input('\nEnter a class, or press enter if you are done: ')

print('\nYou are taking:')
for c in user_classes: # Print all classes
    print(f'\n{c}')