Variables in the code:

'string' is the string the user wishes to change a string from

'change_this' is the string the user wants to change

'change_to' is the string the user wants to change 'change_this' to

'result' is 'string' with all instances of 'change_this' converted to 'change_to'

The following code description will refer to the variables stated before to explain the code:
The main function of the program contains a loop prompting the user for an input. In the loop is a check for given string to figure out if string is empty or contains only spaces. In this case, an error message is printed, and the user is prompted with the same input message as before. If the input is valid, change_words function gets triggered with the user's input as the parameter. In the change_words function, the user is prompted for the string they wish to change. This input is stored in the variable 'change_this'. Similiar check to 'string' is performed, if 'change_this' is empty or contains only spaces, an error message is printed and the program ends. If the input is valid, the user is prompted for what they wish to change the given string to. This input is stored in 'change_to'. Note: 'change_to' can be empty or contain only spaces in which case all instances of 'change_this' are just removed from 'string'. Result stored in 'result' is achieved with string.replace. Result is then printed with an informative message explaining what was changed and to what.
Note: The program is case sensitive. For example, if 'input' contains both 'the' and 'The', and the user wishes to change 'the', then 'The' will not be changed.
