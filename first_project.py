# creating an AI trip planner

enter = int(input("enter 1 to start and 2 to stop!: "))
while enter != 2:
    destination = input("do you have any destination in mind").lower()
    if destination == "yes":
        print("thats good")
        transport = input("plane/train or car").lower()
        if transport == "plane":
            print("great!")
            budget = int(input("what is your budget? "))
            if budget >= 2000:
                print("you can go to Australian beach fo kayaki")
                flight =input("would you like me to book a flight for you? ").lower()
                if flight == "yes":
                    time = input("when would you like to go enter date please ")
                    print(time, "your flight is booked be ready on time")
                    break
                elif flight == "no":
                    print("no problem you can ask me todo it any time")
                    break
            else:
                print("pack your bags and head toward Miami beach:")
                break
        elif transport == "train":
            print("great!")
            budget = int(input("please specify your budget "))
            if budget > 1000 and budget <=1500:
                print("Trip to Germoney will be great!")
                train = input("would you like to book a train ticket for you? ").lower()
                if train == "yes":
                    print("awsome!")
                    time = input("when would you like to go enter date please ")
                    print(time, "your ticket is booked be ready on time")
                    break
                elif train == "no":
                    print("no problem you can ask me todo it any time")
                    break
        elif transport == "car":
            print("wonderfull choice")
            route = input("which direction you would like to go? ")
            print(route, "this time of the year its a good choice")
            stay = input("will you stay in hotels along the route or want to camp road side? ").lower()
            if stay == "hotel":
                booking = input("would you like me book hotels for you? ").lower()
                if booking == "yes":
                    time = input("when would you like to go enter date please ")
                    print(time, "your hotels for stay is booked be ready on time")
                    break
                elif booking == "no":
                    print("no problem you can ask me todo it any time")
                    break
    elif destination == "no":
        print("no problem")
        choices = input("where would you like to go this time beach, riverside, mountains, or city ").lower()
        if choices == "beach":
            print("awsome")
            beach = input("would you like busy or remote? ").lower()
            if beach == "busy":
                print("head towards miami beaches..")
                booking = input("would you like me book hotels for you? ").lower()
                if booking == "yes":
                    time = input("when would you like to go enter date please ")
                    print(time, "your hotels for stay is booked be ready on time")
                    break
                elif booking == "no":
                    print("no problem you can ask me todo it any time")
                    break
            elif beach == "remote":
                print("you can visit florida beaches")
                booking = input("would you like me book hotels for you? ").lower()
                if booking == "yes":
                    time = input("when would you like to go enter date please ")
                    print(time, "your hotels for stay is booked be ready on time")
                    break
                elif booking == "no":
                    print("no problem you can ask me todo it any time")
                    break
        elif choices == "riverside":
            print("awsome")
            river = input("would you like farther north ").lower()
            if beach == "yes":
                print("its good for fishing there.")
                booking = input("would you like me book hotels for you? ").lower()
                if booking == "yes":
                    time = input("when would you like to go enter date please ")
                    print(time, "your hotels for stay is booked be ready on time")
                    break
                elif booking == "no":
                    print("no problem you can ask me todo it any time")
                    break
            elif river == "no":
                print("awsome northen rivers are good for KAyaking")
                booking = input("would you like me book hotels for you? ").lower()
                if booking == "yes":
                    time = input("when would you like to go enter date please ")
                    print(time, "your hotels for stay is booked be ready on time")
                    break
                elif booking == "no":
                    print("no problem you can ask me todo it any time")
                    break
        elif choices == "mountains":
            print("great")
            mountains = input("would you like climbing or hiking ").lower()
            if mountains == "climbing":
                print("its good but little risky.")
                booking = input("are you ready to climb mountains ").lower()
                if booking == "yes":
                    time = input("when would you like to go enter date please ")
                    print(time, "your hotels for stay is booked be ready on time ")
                    break
                elif booking == "no":
                    print("its good to have some training sessions before taking risks")
                    training_class = input("would you like me to book a training session for you")
                    if training_class == "yes":
                        print("wonderfull")
                        print("your session with the best coach is booked you can start from this satuday")
                        break
                    else:
                        print("its ok you can get training on your ease")                    
                        break
            elif mountains == "hiking":
                print("awsome mountains on the southern sides are very good for hiking")
                booking = input("would you like me book hotels for you? ").lower()
                if booking == "yes":
                    time = input("when would you like to go enter date please ")
                    print(time, "your hotels for stay is booked be ready on time ")
                    break
                elif booking == "no":
                    print("no problem you can ask me todo it any time ")
                    break
        elif choices == "city":
            print("wonderfull graet time to socialize")
            choices = input("where would you like to go? ")
            if choices == "thailand":
                print("thailand is good for socializing")
                booking = input("would you like me book hotels for you? ").lower()
                if booking == "yes":
                    time = input("when would you like to go enter date please ")
                    print(time, "your hotels for stay is booked be ready on time ")
                    break
                elif booking == "no":
                    print("no problem you can ask me todo it any time")
                    break
            else:
                print("wonderful")
                booking = input("would you like me book hotels for you? ").lower()
                if booking == "yes":
                    time = input("when would you like to go enter date please ")
                    print(time, "your hotels for stay is booked be ready on time ")
                    break
                elif booking == "no":
                    print("no problem you can ask me todo it any time")
                    break