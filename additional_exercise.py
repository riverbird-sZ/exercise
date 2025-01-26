 name = input("What is your name? ")
print("Hi " + name)
color = input("What is your favourite color? " )
print(name + " likes " + color)

birth_year = input("Birth year: ")
age = 2019 - int(birth_year)
print("This person is " + str(age) + " years old") """
"""
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


'''
min_limit = 3
max_limit = 50

name = input('Enter your name: ')

if len(name) < min_limit:
    print('Name must be at least 3 characters long.')
elif len(name) > max_limit:
    print('Name can be a maximum of 50 characters.')
else:
    print('Name looks good') '''
    
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

