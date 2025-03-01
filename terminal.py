from functions import *



count = int(input("Enter number of people: "))
for i in range(count):
    check_in = input("please enter yes or no: ").lower()
    if check_in == "yes":
        resul = input("Please Enter your Flight budget/ domestic or business : ").lower()
        main_func(resul)
    elif check_in == "no":
        print("no problem you can ask me todo it any time")
