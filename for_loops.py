#invalid character checker 

'''
username = input("Enter your user name ")
invalid = "!@#$%^&*()_+ "

for letter in username:
    if letter in invalid:
        print(f"{letter}this charactor is not allowed ")

print(f"user name is {username}")
'''

# vowel checker and counter
'''
word = input("enter a word")
vowel = "aeiou"
count = 0
for i in word:
    if i in vowel:
        count += 1
        
print(f"vowels in the given words are {count}")
'''
#valid phone number checker
'''
phone_number = input("Enter a valid phone number ").lower()

not_allowed = "abcdefghijklmnopqrstuv !@#$%^&*()_+:;<>?/.,"
for i in phone_number:
    print(i)
    if i in not_allowed:
        print("invalid number")
        break
print(phone_number)
'''
#another way to check valid phone number is "if i not in number" let see
'''
phone_number = input("enter a valid phone number ")
allowed_num = "0123456789"

for i in phone_number:
    if i not in allowed_num:
        print(f"{phone_number} not a valid number")
        break

'''
#allowing guest on the basis of age
'''
guests = int(input("Enter number of guests: "))
for i in range(guests):
    name = input("enter your name: ")
    age = int(input("enter you age in numbers: "))
    if age >= 18:
        print(f"welcome to the party {name}")
    else:
        print(f"{name} you are not allowed to drink")
'''

#valid admin checker

userName = "admin"
password = "12345"

count = 5
tries = 0

for i in range(count):
    tries += 1
    name = input("please enter user name: ")
    inputPassword = input("please enter valid password: ")
    if name ==userName and inputPassword == password:
        print("login succesfull")
        break
    elif tries < 5:
        print("try to enter valid cradentials")
    else: 
        print(f"you attempted {tries} times! you are not an admin !")
        
