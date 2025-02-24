# invoice maker

'''cost = int(input("enter the cost of item: "))
total = 0

while cost != 0:
    total += cost
    cost = int(input("enter cost of item or zero to end: "))
    
print("grand total", total)

discount = total * 0.5
print("discounted price", discount)'''

# pasword checker

'''userInput = input("Enter your pasword: ")
password = "123456"

while userInput != password:
    print("invalid password !")
    userInput = input("please enter a valid password ")
    
print("Login succesfull!")
print("welcome again to your account!")
'''


#multiple choice qustions
'''
test_answer = input("enter a,b,c,d")

tries = 1

while test_answer != "c":
    tries += 1
    print("wrong answer")
    test_answer = input("try again")

print("it took you",tries, "tries to get to the answer")
'''    

#number game
'''
import random

number = int(input("guess a number between 1 to 10 "))
random_number = random.randint(0, 10)
tries = 1

while number != random_number:
    tries += 1
    print("wrong answer")
    number = int(input("try again! guess a number between 1 to 10 "))
    
print("after", tries, "tries you gussed the right number", random_number)
'''

# message bot
'''
input_message = input("please write your message ").lower()

while input_message != "done":
    print("we got your message")
    print("your last message is ", input_message)
    input_message = input("for another message please type your message here or 'done' to exit ")
'''    

# account login

'''
input_password = int(input("enter your password "))

password1 = 123456
password2 = 124578
while input_password != password1 and input_password != password2:
    print("invalid password")
    input_password = int(input("try to enter valid passwrod "))
    
print("welcome to your account")
'''

#offer discount to first three persons

'''
person_count = 0

while person_count < 3:
    person = input("Enter your name ")
    print(f"wow {person} got 20 percent off")
    person_count += 1
    
print("All done")
'''

#AI programming languege guess
'''
guess = input("enter a programming language on which AI is based: ").lower()

count = 0

while guess != "python":
    count += 1
    guess = input("try again")
    
print(f"it took {count} tries to guess Python")
'''

#only have 5 tries
'''
count = 0
guess = ""

while count < 5 and guess != "python":
    guess = input("guess a programming language: ").lower()
    count +=1
    
if guess == "python":
   print(f"it took you {count} tries to guess {guess}")
else:
    print("tries are over")
'''

# train ticket printing 
user_input = int(input("enter 0 to print and 1 to end: "))
ticket_num = 421
count = 0
while user_input != 1:
    print(ticket_num, "is your ticket number")
    ticket_num += 1
    count += 1
    user_input = int(input("enter 0 to print and 1 to end: "))
print(f"done {count} tickets printed")


