names = ["John", "Mark", "Mario"]
print(names)

# Find the biggest number in the list

numbers = [2, 5, 8, 9]
# print(max(numbers))

max = numbers[0]

for number in numbers:
    if number > max:
       max = number
print(max)