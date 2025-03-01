from functions import *


people = int(input("Enter number of people: "))

for i in range(people):
    name = input("Enter your name: ").capitalize()
    weight = float(input("Enter your weight"))
    height = float(input("Enter your height"))
    rest = calculate_bmi(weight, height)
    if rest < 18.5:
        print("Under weight")
    elif rest >=18.5 and rest <=24.9:
        print("normal weight")
    elif rest >=25 and rest <=29.9:
        print("over weight")
    elif rest >=30:
        print("obasity class 1")