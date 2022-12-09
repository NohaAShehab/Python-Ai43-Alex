work = "Information Technology Institute"

print(work[2:8])

print(work[-1])


""" string is immutable datatype """
# print(work[10])

"1- string concatenation ---> is allowed only between strings "
fname = 'Noha '
mid = 'AbdelHady '
lname = "Shehab"
# fullname = fname + mid + mid + lname
# print(fullname)
"2- string interpolation "
fullname = fname + mid*2 + lname
print(fullname)

"3- count no of char occurance in the string "
print(work.count("o"))

"4- string formatting"
# temp = 'My name is {0} I lives in {1}.'  # unlabeled data
# print(temp.format("noha","Cairo"))
# print(temp.format("Ahmed","Alex"))
# print(temp.format("Suez","Andrew"))

# temp = 'My name is {username} I lives in {city}.'
# print(temp.format(username='Ahmed', city='Mansoura'))
# print(temp.format( city='Cairo', username='Mohamed'))
"f- format string...."
# name = 'Noha'
# work = 'iti'
# year = 2022
# temp = f'My name is {name}, I works at {work} {year}.'
# print(temp)

"ask user to enter input "
# name = input("please enter your name: ")  # input function always returns with string
#
# work = input("please enter your work : ")
# message = f"My name is {name}, I works at {work}"
# print(message)

#########################################
"check string content"
# message = 'Hello'
# print(message.isalpha())
#
# year = '2002'
# # print(year.isdigit())  ## Arabic numbers 1 2 3 5
# print(year.isnumeric()) # ## support numbers representation in different languages
#
#
# message = "                       "  # spaces
# print(message.isspace())

################################

message = '                  My name is       Noha                  '
print(len(message))
# strip spaces ---> input email
# message = message.strip() # remove spaces from the beginning and the end of the string
# print(message)
# message = message.lstrip() # remove spaces from the  and the end of the string
# print(message)
# message = message.rstrip() # remove spaces from the  and the end of the string
# print(message)

# mytxt = "# My name is noha #"
# print(mytxt.strip("a# "))  # strip ---> pattern ---> provided to the strip function
# print(mytxt.lstrip("a# "))

#######################
"string replacement..."

msg = "my name is noha , i works at iti"
# print(msg.replace("a", "@"))
print(msg.upper())  # lower
print(msg.isupper())  # islower
print(msg.capitalize())