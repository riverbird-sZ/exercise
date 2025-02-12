import random

"""name = input("What is your name? ")
print("Hi " + name)
color = input("What is your favourite color? " )
print(name + " likes " + color)

birth_year = input("Birth year: ")
age = 2019 - int(birth_year)
print("This person is " + str(age) + " years old")

course = "Python for beginners"
print(len(course))

# Price of a house is $1M. If buyer has a good credit, they need to put down 10%. Otherwise they need to put down 20%. Print the down payment. 

good_credit = True
price = 1000000

if good_credit:
    print("Buyer needs to put down 10%, which is " + str(price * 0.1))
else:
    print("Buyer needs to put down 20%, which is " + str(price * 0.2))
    
has_good_credit = True

if has_good_credit: 
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Buyer needs to put down: ${down_payment}")   

print(down_payment)

# If name is less than 3 characters long, write - name must be at least 3 characters. Otherwise if it is more than 50 chaacters long, write - name can be a maximum of 50 characters. Oterwise "name looks good".

min_limit = 3
max_limit = 50

name = input()

if len(name) < min_limit:
    print('Name must be at least 3 characters long.')
elif len(name) > max_limit:
    print('Name can be a maximum of 50 characters.')
else:
    print('Name looks good')



min_limit = 3
max_limit = 50

name = input('Enter your name: ')

if len(name) < min_limit:
    print('Name must be at least 3 characters long.')
elif len(name) > max_limit:
    print('Name can be a maximum of 50 characters.')
else:
    print('Name looks good')
    
# Weight Converter Program 
# User enters their weight, then program asks is that in kilograms or pounds. After user responds, program converts to other unit.

# solution - not so good

weight = input('What is your weight? ')
unit = input('Is that in kilograms or ponuds? K for kg, L for lbs ')

k = 'k'
l = 'l'


if unit == k:
    conversion_to_pounds = int(weight) * 2.2
    print(f'You have {conversion_to_pounds} pounds.')
elif unit == l:
    conversion_to_kilograms = weight * 0.45
    print(f'You have {round(conversion_to_kilograms, 2)} kilograms.')

# kako radi round funkcija?

# Weight Converter Program 
# User enters their weight, then program asks is that in kilograms or pounds. After user responds, program converts to other unit.

# solution 1:
weight = int(input('What is your weight? '))
unit = input('Is that in kilograms or ponuds? (K for kg, L for lbs) ')

if unit.upper() == 'K':
    conversion_to_pounds = round(int(weight) * 2.2)
    print(f'You have {conversion_to_pounds} pounds.')
elif unit.upper() == 'L':
    conversion_to_kilograms = round(int(weight) * 0.45)
    print(f'You have {conversion_to_kilograms} kilograms.') 

# solution 2:
    
weight = int(input('What is your weight? '))
unit = input('Is that in kilograms or pounds? (K for kilos, L for lbs) ')

if unit.upper() == 'K':
    converted = round(weight * 2.2)
    print(f'You have {converted} pounds.')
else:
    converted = round(weight * 0.45)
    print(f'You have {converted} kilograms.') 

# Guessing game

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Well done, you guessed it!")
        break
    else:
        print("Please try again :)")
    guess_count = guess_count + 1
else:
    print("Sorry, you failed :)") """

# Car game

""" When user enters help, he gets three options: 
 start - to start the car 
 stop - to stop the car
 quit - to exit 

print("start - to start the car")
print("stop - to stop the car")
print("quit - to exit") 

user_input = input("Enter something: ")
help_variable = "HELP"
stop_variable = "STOP"
start_variable = "START"
quit_variable = "QUIT"

while user_input.upper() == help_variable:
    repeated_input = input("What would you like? ")
    if repeated_input.upper() == start_variable:
        print("You started the engine.")
    elif repeated_input.upper() == stop_variable:
        print("You stopped the engine.")
    elif repeated_input.upper == quit_variable:
        print("You quit the engine.")
    else:
        print("I don't understand that.")
else:
    print("I don't understand that.") 



command = ""
started = False

while True:
    command = input("Enter something: ").lower()
    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif command == "help":
    print(start - to start the car
stop - to stop the car quit - to exit
     elif command == "quit": 
        break
    else:
        print("I don't understand. Please try again.") """

"""Calculate total cost of goods in shopping cart"""

""" prices = [10, 10, 30]
total = 0

for price in prices:
    total = sum(prices)
print(total) """

"""total = price + price -> total += price"""

""" Print letter F out of letters X """


""" for number in numbers:
    print("x" * number) """

""" for number in numbers:
    print("x")
    for i in numbers:
        print(numbers[i]) 
         for number in numbers:
        print("x")
        print(numbers[i])
        i += 1
    print("s") 
    print(number, numbers[0])
   i = 0
   for numbers[i] in numbers:
       print("test")
       
  for i < numbers[i]:
        print("X")
    i += 1

    for number in range(len(numbers)):
        print("X")
        
     for numbers[i] in numbers:
        print("xxxxxxx")
        i += 1 

numbers = [5, 2, 5, 2, 2]
a = []
for number in numbers:
     i = 0
     while i < numbers[i]:
         b = a.append("X")
         print(b)
     i += 1


a = range(len(numbers))
print(a)
b = len(numbers)
print(b)
print(numbers[0])
print(numbers[1]) 



 i = 0
     while i < numbers[i]:
         b = a.append("X")
         print(b)
     i += 1
     
     
a = range(len(numbers))
print("range je ", a)
b = len(numbers)
print("duzina niza", b)
print("prvi broj",numbers[0])
print("drugi broj", numbers[1])
x = []


   #print("".join(output))

#b = range(count)
# print(b)
# a = range(numbers[1])
# print(a)

        print(x.append("X"))



GOTOV ZADATAK: 

numbers = [5, 2, 5, 2, 2]

for count in numbers:
    output = ""
    for number in range(count):
       output += "x"
    print(output)



"""











































