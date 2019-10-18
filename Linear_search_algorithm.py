import random

count = 0 ## Keeps track of the indexes it has looked at

numbers = [] ## Initialises the list of numbers

for i in range(0,50):
    '''The range can be changed to generate a larger or smaller amount
    of numbers.'''
    number = random.randint(0,100000)
    numbers.append(number)

print(numbers)
'''Displays the list of numbers the program has randomly generated'''

found = False ## States that the element has not been found yet

search = float(input("Enter a number to search for : "))
while found == False and count < 50:
    if numbers[count] == search:
        found = True
        print("\nFound at position", count + 1)
        count = count + 1
    else:
        count = count + 1
        print("\nNumber not found at index", count)

if found == False:
    print("\nThe number", int(search), "is not in this list.")
    
input("\nPress Enter to exit the program: ")
