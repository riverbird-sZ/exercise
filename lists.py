"""
numbers = [2, 5, 8, 9]
print(numbers.sort())
numbers.reverse()

variable = numbers.copy()
variable.append(30)

print(numbers)
print(variable) """

# Remove duplicates in a list

duplicates = [3, 6, 7, 6]
uniques = []

for number in duplicates:
    if number not in uniques:
        uniques.append(number)
print("Ovo je lista bez duplikata, urađena petljom - ", uniques)


dictionary_of_numbers = dict.fromkeys(duplicates)
list_without_duplicates = list(dictionary_of_numbers)
print("This is a list without duplicates - ", list_without_duplicates)


# Kako napraviti rječnik iz liste

glavno_jelo = "sarma"
predjelo = "supa"
desert = "kolači"

variable = dict(glavno_jelo = "sarma", predjelo = "supa", desert = "kolači")
print(f"Ovo je varijabla - {variable}")

new_variable = dict.fromkeys(glavno_jelo)
print(f"ovo je nova varijabla - {new_variable}")

new_list = ["sarma", "supa", "kolaci", "burgeri"]
my_dictionary = dict.fromkeys(new_list)

print(f"Ovo je prvi rjecnik - {my_dictionary}")

students = ["Ana", "Jana", "Bojana", "Stefan", "Marko", "Ana"]
students_dictionary = dict.fromkeys(students)
print(f"Ovo je zapis studenata {students_dictionary}")

students_new_list = list(students_dictionary)
print(f"Ovo je lista studenata bez duplikata {students_new_list}")






























