age = input("What's your age? ")
print(age)

try:
    user_age = int(input("What's your age? "))
    print(user_age)
except ValueError:
    print("Invalid value!")