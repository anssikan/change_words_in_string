"""Changes all instances of given string, in given string, to given string"""

# This is just to make the user experience more enjoyable
import os
def clear():
    """Clears the screen, command depends on if system is windows or something else"""
    os.system('cls' if os.name=='nt' else 'clear')

def change_words(string):
    """Get what to change, check if string contains it, get what to change to and do it"""
    change_this = str(input("What word would you like to change? "))
    # Check if input is empty or contains only spaces
    if change_this and change_this.strip():
        # Check if "string" contains "change_this"
        if change_this in string:
            clear()
            change_to = str(input("What would you like to change '" + change_this + "' to? "))
            clear()
            result = str(string.replace(change_this, change_to))
            print(f"Text with '{change_this}' converted to '{change_to}' is:\n{result}")
        else:
            clear()
            print("Text doesn't contain the word you wish to change!")
    else:
        clear()
        print("Input was empty or contained only spaces!")

clear()
# Asks for string, keeps asking if input is empty or contains only spaces
while True:
    string = str(input("Input text from which you would like to change a word: "))
    if string and string.strip():
        clear()
        change_words(string)
        break
    else:
        clear()
        print("Input was empty or contained only spaces!")
