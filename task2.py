#!python3

# Reciprocal
# have the user enter numbers and determine the 
# reciprocal of each number as a decimal and print it.
# use the try/except to find any invalid values and display
# the error message

#sample output:
"""
Enter a number: 0
The reciprocal of 0 does not exist
Enter a number: 1
The reciprocal of 1 is 1.0
Enter a number: 2
The reciprocal of 2 is 0.5
Enter a number: 3
The reciprocal of 3 is 0.3333333333333333
Enter a number: 4
The reciprocal of 4 is 0.25
"""
x=float(input("Entere a number: "))

try:
    x1=1/x
    print(f"The reciprocal of {x} is {x1}")
except:
    print(f"The reciprocal of {format(x, '.0f')} does not exist")
