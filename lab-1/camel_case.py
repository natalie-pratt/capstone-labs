import re

"""This program allows a user to enter a sentence of any length (excluding a sentence beginning with a number
    or containing special characters), to be converted into camelCase. User will be asked to enter a different
    sentence if theirs does not conform to conventional format. The sentence will be printed at the end in 
    camelCase if it is in proper format."""

def main():
    
    display_banner()
    user_sentence = input('\nPlease enter a sentence to be converted into camelCase: ')
    user_sentence = validate_sentence(user_sentence) # Validate user sentence using function

    list_of_words = user_sentence.split() # Split sentence into a list of words separated by spaces
    first_word_lowercase = list_of_words[0].lower() # Retrieve first word of sentence, so that it can be fully lowercase

    list_of_camel_words = capitalize_words(list_of_words) # Get list of capitalized words
    camel_case_sentence = join_sentence(list_of_camel_words) # Join list of words into a sentence without spaces
    print_camel_case_sentence(first_word_lowercase, camel_case_sentence)

def display_banner():
    """Display banner at top of program as label for user"""
    msg = "camelCase Program!"
    stars = '*' * len(msg)
    print(f'\n{stars} \n{msg} \n{stars} \n')

def validate_sentence(user_sentence):
    # Using regular expressions, determine whether the sentence begins with a letter or contains special characters, respectively
    while re.match(r"^\d", user_sentence) or re.search(r"[!@#$%^&*(),.?\":{}|<>]", user_sentence): # Regular expression help from https://stackoverflow.com/questions/37531205/check-if-a-string-starts-with-number-using-regular-expression
        print('\ncamelCase convention does not allow sentences beginning with a number or containing special characters.')
        user_sentence = input('Please choose a different sentence: ')
    return user_sentence

def capitalize_words(list_of_words): # Capitalize the first letter of every word - except for the first one
    list_of_camel_words = []

    for word in list_of_words[1:]: 
        word = word.capitalize()
        list_of_camel_words.append(word) # Add to new list of words 
    return list_of_camel_words

def join_sentence(list_of_camel_words):
    camel_case_sentence = ''.join(list_of_camel_words) # Join all words without spaces in between
    return camel_case_sentence

def print_camel_case_sentence(first_word_lowercase, camel_case_sentence):
    print('\nHere is your camelCase sentence:')
    print(f'\n{first_word_lowercase}{camel_case_sentence}') # Join lowercase first word with the rest of the camel-case sentence


main()