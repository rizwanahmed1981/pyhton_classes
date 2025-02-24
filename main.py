# print("hello world")
# print("my","name")
# print(456,5)
# print("Grand Total", 25*8)
# print(25%4) # for modulus
# print(7//3) # for rounded value

# PEMDAS
# perenthesis, exponents, multiplication, division, addition, substraction

# print("send some money", 25*4 + 15*40 + 75-12)

# years = 2
# months = 5
# print("i am being doing cooding since", years , "years", "and ", months, "months")
# print(f"i am being cooding since {years} years and {months} months")

# base_fare = 105
# num_bags = 2
# base_fare = 205
# total_fare = base_fare * (num_bags* 0.6)
# print(total_fare)

# flight_cost = 2500
# insurance = 250
# passport = 5000
# baggage = 2

# # total_cost = 5*((flight_cost+insurance+passport)+(baggage*0.55))
# # print(total_cost)
# adults = 2
# children = 3
# adults_ticket_cost = flight_cost
# children_ticket_cost = flight_cost*0.7

# total_cost = (((adults*(adults*adults_ticket_cost))* baggage*0.55 +5*(insurance+passport) +children*children_ticket_cost))
# print(total_cost)

# resort = 500
# stay_duration = 7
# discounted_resort_cost = stay_duration*resort*0.7

# final_trip_cost = total_cost +discounted_resort_cost

# print(final_trip_cost)

#user info
'''
fName = input("enter your first name: ")
city = input("enter your city: ")
country = input("enter your country: ")

print(f"Mr. {fName} lives in {city} {country}")

carRental = input("Car Rental for one day: ")
numDays = input("number of days car rental required: ")

totalRentalCost = int(carRental) * int(numDays)

print("total cost for car rental for",numDays, "days: " ,totalRentalCost)
'''

#shipment discount
'''
package1 = input("please enter weight of package1: ")
package2 = input("please enter weight of package2: ")
package3 = input("please enter weight of package3: ")
discount = 0.8
totalWeight = (int(package1) + int(package2) + int(package3)) * discount

print(totalWeight)
'''
#nested functions
'''package1 = int(input("please enter weight of package1: "))
package2 = int(input("please enter weight of package2: "))
package3 = int(input("please enter weight of package3: "))
discount = 0.8
totalWeight = (package1 + package2 + package3) * discount

print(totalWeight)
'''
#User id creation
'''
name = input("Enter Name: ")
age = input("Enter Age: ")
idNumber = input("Enter Id number: ")

card = f"""Student Card \n
name:  {name} \n
Age: {age} \n
ID: {idNumber}
"""
print(card)
'''
## len() function is used to calculate the length of a string

'''length = len("Rizwan Ahmed")
print(length)'''


#create an expense tracker

'''income = int(input("Enter Your Income: "))
food_expence = int(input("Enter Your food expence: "))
rent = int(input("Enter Your Rent: "))
otherIncome = int(input("Do u have other income Source: "))

total_income = income + otherIncome
leftOver = total_income - (food_expence + rent)

print("the savings of the month is: ",leftOver)
'''

#over time tracker
'''
salary = int(input("enter your monthly salary: "))
overtime = int(input("total number of extra hours worked: "))
bonus = (salary * 0.2) * overtime
print(bonus)
'''

'''available = int(input("enter available tickets: "))
sold = int(input("enter sold tickets: "))
enough = available > sold
print(enough)'''

# creating a discount program

'''tripType = input("Enter your Trip Type: ").lower()
tripPrice = int(input("Enter Expected Cost: "))
discountCode = input("Enter discount code: ")
if (tripType == "business" and tripPrice >= 1200 and discountCode == "winter23"):
    print("You Are Eligible For Discount of 20%")
else:
    print("you are not eligible for 20% discount")
    '''
    
# Trip suggestion over affordability
'''cost = int(input("Enter your budget: "))

if (cost < 350 ):
    print(f"your budget {cost} is only get you to stay_cation")
elif(cost > 350 and cost < 1000):
    print(f"your budget {cost} is for a road trip")
elif(cost > 1000):
    print("catch a flight to beatch and enjoy")
    '''


#creating cost of luggage based on domastic and international flights
'''bagWeight = int(input("enter weight of the luggage: "))
flightType = input("enter yoyr flight either domastic or international: ").lower()

price = 0

if bagWeight <= 18:
    price += 25
else:
    price += 75

if flightType == "domestic":
    price += 300
elif flightType == "international":
    price += 750

print(price)

'''

# create a mobile suggestion app

'''destination = input("enter destination you want to visit: ").lower()

if destination == "beach":
    print("thailand is the best place to go")
else:
    dream = input("would you like cold or warm: ").lower()
    if dream == "cold":
        print("go for skying in japan1")
    else:
        print("go for mountains hiking in south")
        '''
        
#movie suggestion
'''
userInput = input("do you want to watch a movie now?: ").lower()

if userInput == "yes":
    genre = input("what do you like comedy or something else?: ")
    if genre == "comedy":
        print("Mr bean")
    else:
        print("top gun")
else:
    print("watch a tv serial")
    '''

#hotel and resort suggestions

'''userInput = input("where do you want to stay hotel or resort? ").lower()

if userInput == "hotel":
    price = int(input("what is your budget for per night stay? "))
    if price >= 350:
        print("book a six star hotel")
    else:
        print("you can go for four star hotel")
elif userInput == "resort":
    price = int(input("what is your budget for per night stay? "))
    if price >= 700:
        print("go for miami beach  resorts")
    else:
        print("you should go for a hotel stay")
else:
    print("stay at home and enjoy a hangover party")
    '''
    
    
#Product price based discount

'''pro1Price = int(input("Enter first product price: "))
pro2Price = int(input("Enter 2nd product price: "))
pro3Price = int(input("Enter third product price: "))

if pro1Price < pro2Price and pro2Price < pro3Price:
    total = (pro1Price + pro2Price + pro3Price)* 0.5
elif pro1Price > pro3Price and pro3Price > pro2Price:
    total = (pro1Price + pro2Price + pro3Price)* 0.34

time = int(input("which time you want to get delivered? "))

if time >= 7 and time <=9:
    total = total *0.8
else:
    total = total
    
print(total)'''

# review based program

review = int(input("please rate us between 1 to 9 : "))

if review == 9:
    print("Thank you for your kind review")
elif review >= 5 and review < 9:
    suggestion = input("how can we improve our products and services? ")
    print(suggestion,"!" "we will work hard to improve our products and sevices")
else:
    print("sorry for inconvinience we will improve soon")    