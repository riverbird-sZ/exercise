import utils

kutija = [9, 6, 7]
caos = utils.find_max(kutija)
print(caos)

""" Kada korisnik unese broj telefona, program izbaci broj telefona ispisan riječima. """

user_input = input("Phone: ")
list = ""
numbers = {
"1": "One",
"2": "Two",
"3": "Three",
"4": "Four",
"5": "Five",
"6": "Six",
"7": "Seven",
"8": "Eight",
"9": "Nine",
"0": "Zero"
}

#for number in numbers.keys():
 #   print(number)
    # if govno in numbers.keys():
    # if item == user_input:
      #  list += list
    # print(list)

""" for x, y in numbers.items():
    for item in user_input:
        if x == item:
            list += " " + y
           # variable = " ".join(list)
print(list) """

for ch in user_input:
    list += numbers.get(ch, "!") + " "
print(list)






#for item in user_input:
 #   if (x, y) in numbers.items():
  #      print(x, y)
   #     #list += numbers.values()
    # print(f"Userov input je - ", list)

# 25 min - numbers in words
# 25 min - numbers in words - uspjesno zavrsila





""" for item in user_input:
    if item == numbers.keys():
        list = numbers.values()
        #list.append()
print(list) """