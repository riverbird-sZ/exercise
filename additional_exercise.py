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
