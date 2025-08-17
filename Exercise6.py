#Assignment 5.2

#Task: Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
largest_number = None
smallest_number = None

while True:
    number = input("Enter a number:")
    if(number == 'done'):
        break
    else: 
        try:
            number = int(number)
        except:
            print("Invalid input")
            continue
        if largest_number is None : largest_number = number
        elif number > largest_number: largest_number = number

        if smallest_number is None : smallest_number = number
        elif number < smallest_number: smallest_number = number

print("Maximum is", largest_number)
print("Minimum is", smallest_number)


