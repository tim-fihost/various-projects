#Password Generator 
import string
import random
letters = list(string.ascii_uppercase)
letters = letters + list(string.ascii_lowercase) #letter++
symbols = list('!@#$$%^&*') #symbols
numbers = [0,1,2,3,4,5,6,7,8,9] #numbers
print("Hello I am PyPassword generator!")
amount_of_letter = int(input("How many letters would you like in your password?\n"))
amount_of_symbol = int(input("How many symbols would you like?\n"))
amount_of_number = int (input("How many numbers would you like?\n"))
password_list = []
password = ""
#First Letters
for i in range(0,amount_of_letter):
    password_list.append(letters[random.randint(0,52)]) 
    #an other simple option random.choice(list_name)
#Second Symbols
for i in range(0,amount_of_symbol):
    password_list.append(symbols[random.randint(0,8)])
#Third Numbers
for i in range(0,amount_of_number):
    password_list.append(str(random.randint(1,10)))
random.shuffle(password_list)
for i in password_list:
    password += i
print(password)